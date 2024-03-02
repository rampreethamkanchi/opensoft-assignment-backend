from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import user
from rest_framework import status
from .serializers import username_serializer
from .serializers import user_serializer
from rest_framework.parsers import JSONParser
from .serializers import email_password_serializer
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.conf import settings
@api_view(['GET'])
def username_list(request):
    users = user.objects.all()
    serializer = username_serializer(users, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK) 
@api_view(['GET'])
def verify_usernames(request, username):
    try:
        user.objects.get(username=username)
        return Response({"message": "Username already exists"}, status=status.HTTP_200_OK)
    except user.DoesNotExist:
        return Response({"message": "Username is available"}, status=status.HTTP_200_OK)
@api_view(['GET'])
def verify_credentials(request, email, password):
    try:
        user_details=user.objects.get(email=email, password=password)
        serializer= user_serializer(user_details)
        print(serializer.data)
        print("sending mail")
        emailw = EmailMessage(
            'Hey Ram Preetham Here',
            'You have logged in to the website',
            settings.EMAIL_HOST_USER,
            [email],
        )
        emailw.send(fail_silently=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except user.DoesNotExist:
        return Response({"message":"bad"}, status=status.HTTP_200_OK)
@api_view(['POST'])
def user_registration(request):
    serializer = user_serializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        emailw = EmailMessage(
            'Hey Ram Preetham Here',
            'You are registered to the website',
            settings.EMAIL_HOST_USER,
            [request.data["email"]],
        )
        emailw.send(fail_silently=False)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response({"message":"bad"}, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET'])
def user_detail(request, username):
    try:
        userobject = user.objects.get(username=username)
        serializer = user_serializer(userobject)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except user.DoesNotExist:
        return Response({"message": "User does not exist"}, status=status.HTTP_404_NOT_FOUND)
@api_view(['PUT'])
def user_update(request, username):
    try:
        userobject = user.objects.get(username=username)
        serializer = user_serializer(userobject, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"message": "bad"}, status=status.HTTP_400_BAD_REQUEST)
    except user.DoesNotExist:
        return Response({"message": "User does not exist"}, status=status.HTTP_404_NOT_FOUND)
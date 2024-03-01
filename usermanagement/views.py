from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import user
from rest_framework import status
from .serializers import username_serializer
from .serializers import user_serializer
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
def verify_credentials(request, username, password):
    try:
        user.objects.get(username=username, password=password)
        return Response({"message": "Credentials are correct"}, status=status.HTTP_200_OK)
    except user.DoesNotExist:
        return Response({"message": "Credentials are incorrect"}, status=status.HTTP_200_OK)
@api_view(['POST'])
def add_user(request):
    serializer = user_serializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET'])
def user_detail(request, username):
    try:
        userobject = user.objects.get(username=username)
        serializer = user_serializer(userobject)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except user.DoesNotExist:
        return Response({"message": "User does not exist"}, status=status.HTTP_404_NOT_FOUND)
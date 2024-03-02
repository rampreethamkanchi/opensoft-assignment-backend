"""
URL configuration for usermanagement project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import username_list
from .views import verify_usernames
from .views import verify_credentials
from .views import user_registration
from .views import user_detail
from .views import user_update
# from .views import user_verification
urlpatterns = [
    path('admin/', admin.site.urls),
    path('allusernames/', username_list),
    path('verifyusernames/<str:username>/', verify_usernames),
    path('verifycredentials/<str:email>/<str:password>/', verify_credentials),
    path('userregistration/', user_registration),
    path('userdetail/<str:username>/', user_detail),
    path('userupdate/<str:username>/', user_update),
]

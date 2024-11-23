"""
URL configuration for organiztion project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
from org.views import *
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('org.urls')),
     # Organization management
    path('organizations/', organization_list, name='organization_list'),
    path('organizations/create/', organization_create, name='organization_create'),
    path('organizations/edit/<int:pk>/', organization_edit, name='organization_edit'),
    
    # User management
    path('users/', user_list, name='user_list'),
    path('users/create/', user_create, name='user_create'),
    path('users/assign_role/<int:user_id>/', assign_role, name='assign_role'),

     path('', LoginView.as_view(template_name='registration/login.html'), name='login'),
]

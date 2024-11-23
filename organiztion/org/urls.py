from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('organizations/', views.organization_list, name='organization_list'),
    path('delete/<int:pk>/', views.organization_delete, name='organization_delete'), 
    path('user/<int:user_id>/', views.user_page, name='user_page'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('delete_user/<int:user_id>/', views.delete_user, name='delete_user'),
]

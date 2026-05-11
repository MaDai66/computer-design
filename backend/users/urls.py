from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('profile/', views.profile, name='profile'),
    path('', views.user_list, name='user_list'),
    path('<int:id>/', views.user_detail, name='user_detail'),
    path('<int:id>/toggle-status/', views.toggle_user_status, name='toggle_user_status'),
]

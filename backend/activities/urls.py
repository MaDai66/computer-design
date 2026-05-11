from django.urls import path
from . import views

urlpatterns = [
    path('', views.activity_list, name='activity_list'),
    path('<int:id>/', views.activity_detail, name='activity_detail'),
    path('upcoming/', views.upcoming_activities, name='upcoming_activities'),
]

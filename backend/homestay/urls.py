from django.urls import path
from . import views

urlpatterns = [
    path('', views.homestay_list, name='homestay_list'),
    path('<int:id>/', views.homestay_detail, name='homestay_detail'),
    path('experience/', views.homestay_experience, name='homestay_experience'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.community_list, name='community_list'),
    path('<int:id>/', views.community_detail, name='community_detail'),
    path('travel-note/', views.travel_note, name='travel_note'),
]

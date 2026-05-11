from django.urls import path
from . import views

urlpatterns = [
    path('', views.tour_list, name='tour_list'),
    path('<int:id>/', views.tour_detail, name='tour_detail'),
    path('route/', views.tour_route, name='tour_route'),
]

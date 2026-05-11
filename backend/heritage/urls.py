from django.urls import path
from . import views

urlpatterns = [
    path('', views.heritage_list, name='heritage_list'),
    path('<int:id>/', views.heritage_detail, name='heritage_detail'),
    path('experience/', views.heritage_experience, name='heritage_experience'),
]

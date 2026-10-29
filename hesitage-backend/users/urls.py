from django.urls import path
from .views import UserViewSet

urlpatterns = [
    path('register/', UserViewSet.as_view({'post': 'register'}), name='user_register'),
    path('login/', UserViewSet.as_view({'post': 'login'}), name='user_login'),
    path('logout/', UserViewSet.as_view({'post': 'logout'}), name='user_logout'),
    path('profile/', UserViewSet.as_view({'get': 'profile', 'put': 'update_profile'}), name='user_profile'),
    path('list/', UserViewSet.as_view({'get': 'list'}), name='user_list'),
    path('<int:pk>/', UserViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='user_detail'),
    path('<int:pk>/toggle-status/', UserViewSet.as_view({'post': 'toggle_status'}), name='toggle_user_status'),
]
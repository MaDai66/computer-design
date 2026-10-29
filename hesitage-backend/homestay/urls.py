from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    HomestayViewSet, HomestayRoomViewSet,
    HomestayExperienceViewSet, HomestayReviewViewSet
)

router = DefaultRouter()
router.register(r'rooms', HomestayRoomViewSet, basename='homestay-room')
router.register(r'experiences', HomestayExperienceViewSet, basename='homestay-experience')
router.register(r'reviews', HomestayReviewViewSet, basename='homestay-review')
router.register(r'', HomestayViewSet, basename='homestay')

urlpatterns = [
    path('', include(router.urls)),
]

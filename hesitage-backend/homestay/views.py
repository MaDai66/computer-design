from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Homestay, HomestayRoom, HomestayExperience, HomestayReview
from .serializers import (
    HomestaySerializer, HomestayRoomSerializer,
    HomestayExperienceSerializer, HomestayReviewSerializer
)


class HomestayViewSet(viewsets.ModelViewSet):
    queryset = Homestay.objects.all()
    serializer_class = HomestaySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    search_fields = ['name', 'description', 'location']
    filterset_fields = ['area', 'has_heritage', 'self_operated', 'hot']
    ordering_fields = ['price', 'rating', 'created_at']


class HomestayRoomViewSet(viewsets.ModelViewSet):
    queryset = HomestayRoom.objects.all()
    serializer_class = HomestayRoomSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filterset_fields = ['homestay']


class HomestayExperienceViewSet(viewsets.ModelViewSet):
    queryset = HomestayExperience.objects.all()
    serializer_class = HomestayExperienceSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filterset_fields = ['homestay']


class HomestayReviewViewSet(viewsets.ModelViewSet):
    queryset = HomestayReview.objects.all()
    serializer_class = HomestayReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filterset_fields = ['homestay']
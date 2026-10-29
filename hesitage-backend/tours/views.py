from rest_framework import viewsets, serializers, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Tour, TourDay, TimeSlot, HeritageHighlight, CostInfo, TourReview
from .serializers import (
    TourSerializer, TourDaySerializer, TimeSlotSerializer,
    HeritageHighlightSerializer, CostInfoSerializer, TourReviewSerializer
)

class TourViewSet(viewsets.ModelViewSet):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    search_fields = ['name', 'description']
    ordering_fields = ['price', 'rating', 'created_at']

class TourDayViewSet(viewsets.ModelViewSet):
    queryset = TourDay.objects.all()
    serializer_class = TourDaySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class TimeSlotViewSet(viewsets.ModelViewSet):
    queryset = TimeSlot.objects.all()
    serializer_class = TimeSlotSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class HeritageHighlightViewSet(viewsets.ModelViewSet):
    queryset = HeritageHighlight.objects.all()
    serializer_class = HeritageHighlightSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class CostInfoViewSet(viewsets.ModelViewSet):
    queryset = CostInfo.objects.all()
    serializer_class = CostInfoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class TourReviewViewSet(viewsets.ModelViewSet):
    queryset = TourReview.objects.all()
    serializer_class = TourReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        tour_id = serializer.validated_data.pop('tour_id')
        try:
            tour = Tour.objects.get(pk=tour_id)
            serializer.save(tour=tour)
        except Tour.DoesNotExist:
            raise serializers.ValidationError({"tour_id": "Tour does not exist"})


@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def get_tour_reviews(request, tour_id):
    try:
        tour = Tour.objects.get(pk=tour_id)
        reviews = TourReview.objects.filter(tour=tour)
        serializer = TourReviewSerializer(reviews, many=True)
        return Response(serializer.data)
    except Tour.DoesNotExist:
        return Response({"error": "Tour does not exist"}, status=status.HTTP_404_NOT_FOUND)
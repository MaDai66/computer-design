from rest_framework import serializers
from .models import Tour, TourDay, TimeSlot, HeritageHighlight, CostInfo, TourReview

class TimeSlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeSlot
        fields = ['id', 'time', 'activity', 'description']

class HeritageHighlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeritageHighlight
        fields = ['id', 'icon', 'title', 'description']

class CostInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CostInfo
        fields = ['id', 'includes', 'excludes', 'booking_notes']

class TourDaySerializer(serializers.ModelSerializer):
    time_slots = TimeSlotSerializer(many=True, read_only=True)

    class Meta:
        model = TourDay
        fields = ['id', 'day_number', 'title', 'time_slots']

class TourReviewSerializer(serializers.ModelSerializer):
    date = serializers.DateField(format='%Y-%m-%d', read_only=True)
    tour_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = TourReview
        fields = ['id', 'tour_id', 'user_name', 'avatar', 'rating', 'content', 'images', 'date']

class TourSerializer(serializers.ModelSerializer):
    days = TourDaySerializer(many=True, read_only=True)
    highlights = HeritageHighlightSerializer(many=True, read_only=True)
    cost_info = CostInfoSerializer(read_only=True)
    reviews = TourReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Tour
        fields = [
            'id', 'name', 'description', 'image', 'image_base64', 'gallery_base64',
            'duration', 'price', 'experience_points', 'rating', 'review_count',
            'sales_count', 'tags', 'days', 'highlights', 'cost_info', 'reviews', 'created_at'
        ]
        read_only_fields = ['rating', 'review_count', 'sales_count', 'created_at']
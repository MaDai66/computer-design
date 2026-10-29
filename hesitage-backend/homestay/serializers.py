from rest_framework import serializers
from .models import Homestay, HomestayRoom, HomestayExperience, HomestayReview


class HomestayRoomSerializer(serializers.ModelSerializer):
    homestay = serializers.PrimaryKeyRelatedField(
        queryset=Homestay.objects.all(),
        write_only=True,
        required=True
    )
    
    class Meta:
        model = HomestayRoom
        fields = ['id', 'homestay', 'name', 'image', 'description', 'price', 'capacity']


class HomestayExperienceSerializer(serializers.ModelSerializer):
    homestay = serializers.PrimaryKeyRelatedField(
        queryset=Homestay.objects.all(),
        write_only=True,
        required=True
    )
    
    class Meta:
        model = HomestayExperience
        fields = ['id', 'homestay', 'name', 'image', 'description', 'duration', 'price']


class HomestayReviewSerializer(serializers.ModelSerializer):
    homestay = serializers.PrimaryKeyRelatedField(
        queryset=Homestay.objects.all(),
        write_only=True,
        required=True
    )
    
    class Meta:
        model = HomestayReview
        fields = ['id', 'homestay', 'user_name', 'avatar', 'rating', 'content', 'date']


class HomestaySerializer(serializers.ModelSerializer):
    rooms = HomestayRoomSerializer(many=True, read_only=True)
    experiences = HomestayExperienceSerializer(many=True, read_only=True)
    reviews = HomestayReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Homestay
        fields = [
            'id', 'name', 'description', 'image', 'images',
            'price', 'rating', 'review_count',
            'location', 'distance', 'area',
            'has_heritage', 'self_operated', 'hot',
            'facilities', 'created_at',
            'rooms', 'experiences', 'reviews'
        ]
        read_only_fields = ['created_at']
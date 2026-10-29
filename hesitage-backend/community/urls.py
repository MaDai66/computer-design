from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CommunityPostViewSet, PostCommentViewSet

router = DefaultRouter()
router.register(r'comments', PostCommentViewSet, basename='post-comment')
router.register(r'', CommunityPostViewSet, basename='community-post')

urlpatterns = [
    path('', include(router.urls)),
]

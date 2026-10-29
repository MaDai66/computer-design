from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from .models import CommunityPost, PostComment
from .serializers import (
    CommunityPostSerializer,
    CommunityPostListSerializer,
    CommunityPostCreateSerializer,
    PostCommentSerializer,
    PostCommentCreateSerializer
)


class CommunityPostViewSet(viewsets.ModelViewSet):
    queryset = CommunityPost.objects.all()
    permission_classes = [AllowAny]
    search_fields = ['title', 'content']
    ordering_fields = ['created_at', 'likes']

    def get_serializer_class(self):
        if self.action == 'create':
            return CommunityPostCreateSerializer
        elif self.action == 'list':
            return CommunityPostListSerializer
        return CommunityPostSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        post = serializer.save()

        response_serializer = CommunityPostSerializer(post)
        return Response(response_serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['get'])
    def detail(self, request, pk=None):
        post = self.get_object()
        post.views += 1
        post.save()
        serializer = CommunityPostSerializer(post)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        post = self.get_object()
        post.likes += 1
        post.save()
        return Response({
            'message': '点赞成功',
            'likes': post.likes
        })

    @action(detail=True, methods=['post'])
    def add_comment(self, request, pk=None):
        post = self.get_object()
        serializer = PostCommentCreateSerializer(data=request.data)
        if serializer.is_valid():
            comment = serializer.save(post=post)
            post.comments += 1
            post.save()
            response_serializer = PostCommentSerializer(comment)
            return Response(response_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostCommentViewSet(viewsets.ModelViewSet):
    queryset = PostComment.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.action == 'create':
            return PostCommentCreateSerializer
        return PostCommentSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        comment = serializer.save()
        
        # 更新帖子的评论数
        post = comment.post
        post.comments += 1
        post.save()
        
        response_serializer = PostCommentSerializer(comment)
        return Response(response_serializer.data, status=status.HTTP_201_CREATED)
    
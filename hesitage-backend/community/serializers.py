from rest_framework import serializers
from .models import CommunityPost, PostComment
from users.models import User


class PostCommentSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format='%Y-%m-%d', read_only=True)

    class Meta:
        model = PostComment
        fields = ['id', 'user_name', 'avatar', 'content', 'likes', 'created_at']


class PostCommentCreateSerializer(serializers.ModelSerializer):
    post = serializers.IntegerField(write_only=True)

    class Meta:
        model = PostComment
        fields = ['post', 'user_name', 'avatar', 'content', 'likes']

    def create(self, validated_data):
        post_id = validated_data.pop('post')
        try:
            post = CommunityPost.objects.get(id=post_id)
            validated_data['post'] = post
        except CommunityPost.DoesNotExist:
            raise serializers.ValidationError({'post': 'Post not found'})
        return super().create(validated_data)


class CommunityPostSerializer(serializers.ModelSerializer):
    post_comments = PostCommentSerializer(many=True, read_only=True)
    created_at = serializers.DateTimeField(format='%Y-%m-%d', read_only=True)

    class Meta:
        model = CommunityPost
        fields = [
            'id', 'title', 'content', 'image', 'images',
            'likes', 'comments', 'views',
            'author_name', 'author_avatar',
            'created_at', 'post_comments'
        ]


class CommunityPostListSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format='%Y-%m-%d', read_only=True)

    class Meta:
        model = CommunityPost
        fields = [
            'id', 'title', 'image', 'likes', 'comments', 'views',
            'author_name', 'author_avatar', 'created_at'
        ]


class CommunityPostCreateSerializer(serializers.ModelSerializer):
    post_comments = PostCommentCreateSerializer(many=True, required=False)
    created_at = serializers.DateTimeField(format='%Y-%m-%d', read_only=True)

    class Meta:
        model = CommunityPost
        fields = [
            'id', 'title', 'content', 'image', 'images',
            'likes', 'comments', 'views',
            'author_name', 'author_avatar',
            'created_at', 'post_comments'
        ]
        read_only_fields = ['likes', 'comments', 'views']

    def create(self, validated_data):
        post_comments_data = validated_data.pop('post_comments', [])
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            validated_data['user'] = request.user
        else:
            user, created = User.objects.get_or_create(
                username='default_user',
                defaults={'email': 'default@example.com'}
            )
            validated_data['user'] = user
        if not validated_data.get('author_name'):
            if request and request.user.is_authenticated:
                validated_data['author_name'] = request.user.username
            else:
                validated_data['author_name'] = '@匿名用户'
        post = CommunityPost.objects.create(**validated_data)
        for comment_data in post_comments_data:
            post_id = comment_data.pop('post', None)
            PostComment.objects.create(post=post, **comment_data)
        return post

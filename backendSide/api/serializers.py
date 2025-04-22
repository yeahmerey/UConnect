# serializers.py
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Post, Profile, Comment

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']
        extra_kwargs = {
            'email': {'required': True}
        }


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = ['id', 'user', 'bio', 'avatar']


class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    comments_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'user', 'content', 'created_at', 'comments_count']

    def get_comments_count(self, obj):
        return Comment.objects.filter(post=obj).count()


class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    post = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'user', 'post', 'content', 'created_at']


# authentication.py
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.conf import settings


class BearerTokenAuthentication(JWTAuthentication):
    """
    Custom authentication class that validates Bearer tokens in the Authorization header
    """

    def get_header(self, request):
        header = super().get_header(request)
        if header and header.decode('utf-8').startswith('Bearer '):
            return header
        return None

    def get_raw_token(self, header):
        if header is None:
            return None
        parts = header.decode('utf-8').split()
        if len(parts) == 2 and parts[0] == 'Bearer':
            return parts[1]
        return None
from rest_framework import serializers 
from .models import Post , Comment 
from users.serializers import UserProfileSerializer

class PostSerializer(serializers.ModelSerializer) :
    author = UserProfileSerializer(read_only=True)
    class Meta : 
        model = Post 
        fields = ['id', 'author', 'title', 'content', 'created_at']

class CommentSerializer(serializers.ModelSerializer):
    author = UserProfileSerializer(read_only=True)

    class Meta :
        model = Comment 
        fields = ['id', 'post', 'author', 'content', 'created_at']

class CreateCommentSerializer(serializers.Serializer):
    post_id = serializers.IntegerField()
    content = serializers.CharField()
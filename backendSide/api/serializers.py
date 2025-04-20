from rest_framework import serializers
from .models import Post , Profile , Comment

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField()
    email = serializers.EmailField()

class CommentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    user = UserSerializer(read_only=True)
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())
    content = serializers.CharField()
    created_at = serializers.DateTimeField(read_only=True)

    def create(self , validated_data):
        return Comment.objects.create(**validated_data)

class ProfileSerializer(serializers.ModelSerializer) :
    user = UserSerializer(read_only=True)

    class Meta : 
        model = Profile 
        fields = ['id' , 'user', 'bio' , 'avatar']

class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta : 
        model = Post
        fields = ['id' , 'user' , 'content' , 'created_at']
        
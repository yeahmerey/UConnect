from django.shortcuts import render
from .models import Post , Comment 
from rest_framework import status
from users.models import UserProfie
from .serializers import PostSerializer , CommentSerializer , CreateCommentSerializer
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny

class PostListAndPostCreateView(APIView):
    @permission_classes([IsAuthenticated])
    def get(self , request) : 
        posts = Post.objects.all().order_by('-created_at')
        serializer = PostSerializer(posts , many=True)
        return Response(serializer.data)
    
    @permission_classes([IsAuthenticated])
    def post(self , request) : 
        user_profile = UserProfie.objects.get(user=request.user)

        serializer = PostSerializer(data=request.data)
        if serializer.is_valid() :
            serializer.save(author=user_profile)
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    
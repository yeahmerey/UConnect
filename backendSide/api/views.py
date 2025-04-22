# views.py
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from .models import Profile, Post, Comment
from .serializers import (
    UserSerializer,
    CommentSerializer,
    ProfileSerializer,
    PostSerializer
)

User = get_user_model()


# Auth Views
@api_view(['POST'])
def register(request):
    """Регистрация пользователя"""
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = User.objects.create_user(
            username=serializer.validated_data['username'],
            email=serializer.validated_data['email'],
            password=request.data.get('password')
        )
        Profile.objects.create(user=user)
        refresh = RefreshToken.for_user(user)
        return Response({
            'user': UserSerializer(user).data,
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout(request):
    """Выход из системы"""
    try:
        refresh_token = request.data["refresh"]
        token = RefreshToken(refresh_token)
        token.blacklist()
        return Response(status=status.HTTP_205_RESET_CONTENT)
    except Exception as e:
        print(str(e))
        return Response(status=status.HTTP_400_BAD_REQUEST)


class ProfileView(APIView):
    """Профиль пользователя"""
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, user_id=None):
        user = request.user if user_id is None else get_object_or_404(User, id=user_id)
        profile = get_object_or_404(Profile, user=user)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)

    def patch(self, request):
        profile = get_object_or_404(Profile, user=request.user)
        serializer = ProfileSerializer(profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# New Post CRUD views
class PostListCreateView(APIView):
    """Список всех постов и создание нового поста"""
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        posts = Post.objects.all().order_by('-created_at')
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostDetailView(APIView):
    """Детали, обновление и удаление поста"""
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, post_id):
        return get_object_or_404(Post, id=post_id)

    def get(self, request, post_id):
        post = self.get_object(post_id)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def put(self, request, post_id):
        post = self.get_object(post_id)
        if post.user != request.user:
            return Response({"detail": "You don't have permission to edit this post."},
                            status=status.HTTP_403_FORBIDDEN)

        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, post_id):
        post = self.get_object(post_id)
        if post.user != request.user:
            return Response({"detail": "You don't have permission to edit this post."},
                            status=status.HTTP_403_FORBIDDEN)

        serializer = PostSerializer(post, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, post_id):
        post = self.get_object(post_id)
        if post.user != request.user:
            return Response({"detail": "You don't have permission to delete this post."},
                            status=status.HTTP_403_FORBIDDEN)

        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserPostsView(APIView):
    """Получение постов конкретного пользователя"""
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, user_id=None):
        user = request.user if user_id is None else get_object_or_404(User, id=user_id)
        posts = Post.objects.filter(user=user).order_by('-created_at')
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)


class PostCommentsView(APIView):
    """Комментарии к посту"""
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_post(self, post_id):
        return get_object_or_404(Post, id=post_id)

    def get(self, request, post_id):
        post = self.get_post(post_id)
        comments = Comment.objects.filter(post=post)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request, post_id):
        post = self.get_post(post_id)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user, post=post)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentDetailView(APIView):
    """Детали, обновление и удаление комментария"""
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, comment_id):
        return get_object_or_404(Comment, id=comment_id)

    def get(self, request, post_id, comment_id):
        comment = self.get_object(comment_id)
        if comment.post.id != post_id:
            return Response({"detail": "Comment does not belong to this post"},
                            status=status.HTTP_400_BAD_REQUEST)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    def put(self, request, post_id, comment_id):
        comment = self.get_object(comment_id)
        if comment.post.id != post_id:
            return Response({"detail": "Comment does not belong to this post"},
                            status=status.HTTP_400_BAD_REQUEST)
        if comment.user != request.user:
            return Response({"detail": "You don't have permission to edit this comment."},
                            status=status.HTTP_403_FORBIDDEN)

        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, post_id, comment_id):
        comment = self.get_object(comment_id)
        if comment.post.id != post_id:
            return Response({"detail": "Comment does not belong to this post"},
                            status=status.HTTP_400_BAD_REQUEST)
        if comment.user != request.user:
            return Response({"detail": "You don't have permission to delete this comment."},
                            status=status.HTTP_403_FORBIDDEN)

        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
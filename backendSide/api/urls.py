from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import (
    register,
    logout,
    ProfileView,
    PostListCreateView,
    PostDetailView,
    UserPostsView,
    PostCommentsView,
    CommentDetailView
)

urlpatterns = [
    # Auth
    path('auth/register/', register, name='register'),
    path('auth/login/', TokenObtainPairView.as_view(), name='login'),
    path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/logout/', logout, name='logout'),

    # Profile
    path('my/', ProfileView.as_view(), name='profile'),
    path('profile/<str:username>/', ProfileView.as_view(), name='user-profile'),
    path('profile/<str:username>/posts/', UserPostsView.as_view(), name='user-posts'),
    path('my/posts/', UserPostsView.as_view(), name='my-posts'),

    # Posts - independent CRUD
    path('posts/', PostListCreateView.as_view(), name='posts-list'),
    path('posts/<int:post_id>/', PostDetailView.as_view(), name='post-detail'),

    path('posts/<int:post_id>/comments/', PostCommentsView.as_view(), name='post-comments'),
    path('posts/<int:post_id>/comments/<int:comment_id>/', CommentDetailView.as_view(), name='comment-detail'),
]
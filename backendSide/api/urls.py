from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import (
    register,
    logout,
    ProfileView,
    PostView,
    PostCommentsView,
    CommentDetailView
)

urlpatterns = [
    # Auth
    path('register/', register, name='register'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', logout, name='logout'),

    # Profile
    path('profile/', ProfileView.as_view(), name='profile'),

    # Posts
    path('posts/', PostView.as_view(), name='posts-list'),
    path('posts/<int:post_id>/', PostView.as_view(), name='post-detail'),
    path('users/<int:user_id>/posts/', PostView.as_view(), name='user-posts'),

    # Comments (вложенные)
    path('users/<int:user_id>/posts/<int:post_id>/comments/',
         PostCommentsView.as_view(), name='post-comments'),
    path('users/<int:user_id>/posts/<int:post_id>/comments/<int:comment_id>/',
         CommentDetailView.as_view(), name='comment-detail'),
]
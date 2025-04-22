from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import (
    register,
    logout,
    ProfileView,
    PostView,
    PostCommentsView,
    CommentDetailView, get_all_posts, get_post_by_id
)

urlpatterns = [
    # Auth
    path('register/', register, name='register'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', logout, name='logout'),

    # Profile
    path('profile/', ProfileView.as_view(), name='profile'),

    path('profile/<int:user_id>/', ProfileView.as_view(), name='profile'),

    # Posts
    path('posts/', get_all_posts, name='posts-list'),
    path('posts/<int:post_id>/', get_post_by_id, name='post-detail'),
    path('profile/posts', PostView.as_view(), name='user-post-comments'),
    path('profile/<int:user_id>/posts/', PostView.as_view(), name='user-posts'),
    path('profile/<int:user_id>/posts/<int:post_id>/comments/',
         PostCommentsView.as_view(), name='post-comments'),
    path('profile/<int:user_id>/posts/<int:post_id>/comments/<int:comment_id>/',
         CommentDetailView.as_view(), name='comment-detail'),
]
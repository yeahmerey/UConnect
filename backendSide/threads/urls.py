from django.urls import path 
from . import views
urlpatterns = [
    path('posts/' , views.PostListAndPostCreateView.as_view()), 
]

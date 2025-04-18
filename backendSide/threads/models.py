from django.db import models
from users.models import UserProfie
 

class Post(models.Model) : 
    author = models.ForeignKey(UserProfie , on_delete=models.CASCADE , related_name='posts')
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title 

class Comment(models.Model):
    post = models.ForeignKey(Post , on_delete=models.CASCADE , related_name='comments')
    author = models.ForeignKey(UserProfie , on_delete=models.CASCADE , related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.author.user.username}'
    
    
from django.db import models
from django.contrib.auth.models import User

#Models : User(встроенный модель)

class Profile(models.Model) :
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatars/' , blank=True, null=True)

    def __str__(self):
        return self.user.username 


class Post(models.Model) :
    user = models.ForeignKey(User , on_delete=models.CASCADE , related_name='posts')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return f"{self.user.username} - {self.created_at.strftime('%Y-%m-%d %H:%M')}" 


class Comment(models.Model) :
    user = models.ForeignKey(User , on_delete=models.CASCADE , related_name='comments')
    post = models.ForeignKey(Post , on_delete=models.CASCADE , related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.post.id}"
    


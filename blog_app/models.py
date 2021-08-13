from django.db import models
from django.db.models.deletion import CASCADE
from django.utils import timezone
from django.contrib.auth.models import User



class Post(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    section = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)
    last_modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comment', on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name='records', on_delete=models.CASCADE)
    opinion = models.TextField()

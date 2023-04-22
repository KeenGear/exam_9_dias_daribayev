import os

from django.contrib.auth.models import User
from django.db import models


def upload_to(instance, filename):
    # remove path separators from filename
    filename = os.path.basename(filename)
    return f'uploads/user_{instance.author.id}/{filename:5}'


# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User, related_name='gallery_post', on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    image = models.ImageField(upload_to=upload_to)
    created_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    favorite = models.ManyToManyField(User, related_name='favorite_posts', blank=True)

    def __str__(self):
        return f'{self.user} ({self.created_at:%d-%m-%Y %H:%M}) {self.text}'

    class Meta:
        ordering = ['-created_at']

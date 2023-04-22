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
    image = models.ImageField(upload_to=upload_to, null=False, blank=False)
    created_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    favorite = models.ManyToManyField(User, related_name='favorite_posts', blank=True)

    def __str__(self):
        return f'{self.user} ({self.created_at:%d-%m-%Y %H:%M}) {self.text}'

    class Meta:
        ordering = ['-created_at']

    def get_image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=upload_to, null=True, blank=True)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.post} {self.text}'

    def get_image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url

import os

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


def upload_to(instance, filename):
    # remove path separators from filename
    filename = os.path.basename(filename)
    return f'uploads/user_profiles/user_{instance.user.id}/{filename:2}'


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follows = models.ManyToManyField('self', related_name='followed_by', symmetrical=False, blank=True)
    updated_at = models.DateTimeField(User, auto_now=True)
    profile_pic = models.ImageField(null=True, blank=True, upload_to=upload_to, verbose_name='profile_pic')

    def __str__(self):
        return f'{self.user.username}'


# Create Profile When New User Sign Up
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()
        # Have The User Follow themselves
        user_profile.follows.set([instance.profile.id])
        user_profile.save()

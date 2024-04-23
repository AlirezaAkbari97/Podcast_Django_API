from django.contrib.auth.models import AbstractUser
from django.db import models



class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.username


class Channel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos', blank=True, null=True)
    following_channels = models.ManyToManyField(Channel, related_name='followers', blank=True)

    def __str__(self):
        return self.user.username

class FollowedChannel(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    channel = models.OneToOneField(Channel, on_delete=models.CASCADE)
    followed_at = models.DateTimeField(auto_now_add=True)

    unique_together = ('user','channel',)
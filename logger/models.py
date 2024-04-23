from django.db import models

# Create your models here.
from django.db import models
from user_panel.models import CustomUser
from content.models import Episode
from user_panel.models import Channel


class ViewedContent(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    episode = models.ForeignKey(Episode, on_delete=models.CASCADE)
    viewed_at = models.DateTimeField(auto_now_add=True)


class ViewedChannel(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    viewed_at = models.DateTimeField(auto_now_add=True)

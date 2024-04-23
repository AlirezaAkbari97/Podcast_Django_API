from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Episode(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    channel = models.ForeignKey('user_panel.Channel', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    audio_file = models.FileField(upload_to='episode_audio/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


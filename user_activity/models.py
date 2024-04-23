# from django.db import models
# from django.contrib.auth import get_user_model
# from content.models import Episode
# from user_panel.models import Channel

# User = get_user_model()


# class Comment(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     episode = models.ForeignKey(Episode, on_delete=models.CASCADE)
#     content = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)


# class Like(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     episode = models.ForeignKey(Episode, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)


# class Playlist(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     name = models.CharField(max_length=255)
#     episodes = models.ManyToManyField(Episode, through='PlaylistItem')


# class PlaylistItem(models.Model):
#     playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)
#     episode = models.ForeignKey(Episode, on_delete=models.CASCADE)
#     added_at = models.DateTimeField(auto_now_add=True)


# class FollowedChannel(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
#     followed_at = models.DateTimeField(auto_now_add=True)

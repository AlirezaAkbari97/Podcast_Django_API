from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from content.models import Episode
from user_panel.models import Channel
from .models import ViewedContent, ViewedChannel


@receiver(post_save, sender=Episode)
def log_viewed_content(sender, instance, created, **kwargs):
    if created:
        User = get_user_model()
        users = User.objects.all()
        for user in users:
            ViewedContent.objects.create(user=user, episode=instance)


@receiver(post_save, sender=Channel)
def log_viewed_channel(sender, instance, created, **kwargs):
    if created:
        User = get_user_model()
        users = User.objects.all()
        for user in users:
            ViewedChannel.objects.create(user=user, channel=instance)

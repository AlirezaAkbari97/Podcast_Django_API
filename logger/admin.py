from django.contrib import admin
from .models import ViewedContent, ViewedChannel


@admin.register(ViewedContent)
class ViewedContentAdmin(admin.ModelAdmin):
    list_display = ('user', 'episode', 'viewed_at')
    list_filter = ('user', 'episode', 'viewed_at')
    search_fields = ('user__username', 'episode__title')
    date_hierarchy = 'viewed_at'


@admin.register(ViewedChannel)
class ViewedChannelAdmin(admin.ModelAdmin):
    list_display = ('user', 'channel', 'viewed_at')
    list_filter = ('user', 'channel', 'viewed_at')
    search_fields = ('user__username', 'channel__name')
    date_hierarchy = 'viewed_at'

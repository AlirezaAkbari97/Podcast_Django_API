from django.contrib import admin
from .models import Episode

@admin.register(Episode)
class EpisodeAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'channel', 'author', 'created_at')
    list_filter = ('channel', 'author', 'created_at')
    search_fields = ('title', 'description')
    date_hierarchy = 'created_at'

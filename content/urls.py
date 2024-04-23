from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import EpisodeViewSet, MentionAPIView, ChannelEpisodesAPIView, EpisodeDetailAPIView, EpisodePlaybackAPIView

router = DefaultRouter()
router.register(r'episodes', EpisodeViewSet, basename='episode')

urlpatterns = [
    path('episodes/<int:pk>/mention/', MentionAPIView.as_view(), name='mention'),
    path('channels/<int:channel_id>/episodes/', ChannelEpisodesAPIView.as_view(), name='channel-episodes'),
    path('episodes/<int:pk>/', EpisodeDetailAPIView.as_view(), name='episode-detail'),
    path('episodes/<int:pk>/playback/', EpisodePlaybackAPIView.as_view(), name='episode-playback'),
]

urlpatterns += router.urls

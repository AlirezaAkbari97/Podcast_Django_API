from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ViewedContentViewSet, ViewedChannelViewSet

router = DefaultRouter()
router.register(r'viewed-content', ViewedContentViewSet, basename='viewed-content')
router.register(r'viewed-channel', ViewedChannelViewSet, basename='viewed-channel')

urlpatterns = [
    path('', include(router.urls)),
]

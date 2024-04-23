from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import ViewedContent, ViewedChannel
from .serializers import ViewedContentSerializer, ViewedChannelSerializer
from datetime import datetime


class ViewedContentViewSet(viewsets.ModelViewSet):
    queryset = ViewedContent.objects.all()
    serializer_class = ViewedContentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, viewed_at=datetime.now())


class ViewedChannelViewSet(viewsets.ModelViewSet):
    queryset = ViewedChannel.objects.all()
    serializer_class = ViewedChannelSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, viewed_at=datetime.now())

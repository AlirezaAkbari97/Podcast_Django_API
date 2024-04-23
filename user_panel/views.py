from rest_framework import generics, status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from user_panel.models import CustomUser, FollowedChannel, Profile, Channel
from .serializers import FollowedChannelSerializer, UserSerializer, RegisterSerializer, ProfileSerializer, ChannelSerializer
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from content.models import Episode
from user_panel.models import Channel
from logger.models import ViewedContent, ViewedChannel
from rest_framework import viewsets, mixins

class RegisterUserApi(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        Profile.objects.create(user=user)

        token, _ = Token.objects.get_or_create(user=serializer.instance)
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data
        })


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Profile.objects.filter(user=self.request.user)


class FollowChannelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer
    permission_classes = [IsAuthenticated]


class FollowedChannelAPIView(generics.ListAPIView):
    serializer_class = ChannelSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.request.user.following_channels.all()

# Appyly that user just see her/his channel that followed
class FollowedChannelViewSet(viewsets.ModelViewSet):
    queryset = FollowedChannel.objects.all()
    serializer_class = FollowedChannelSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return FollowedChannel.objects.filter(user = self.request.user)
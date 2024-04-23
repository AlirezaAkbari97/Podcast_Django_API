from django.urls import path
from user_panel.views import *
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import routers

router = routers.DefaultRouter()
# Edit Profile
router.register(r'profile', ProfileViewSet, basename='user-profile')
router.register(r'ChannelList', FollowChannelViewSet, basename='ChannelList')
# Follow/Unfoloow Channel
router.register(r'followed-channels', FollowedChannelViewSet, basename='followedchannel')

# Show Detail of Channels
router.register(r'Channel-Details', FollowChannelViewSet, basename='Channel-Details')

urlpatterns = router.urls
urlpatterns += [
    path('register/', RegisterUserApi.as_view(), name='register'),
    path('login/', obtain_auth_token, name='login'),
]

from django.contrib import admin
from django.urls import path,include
from podcastPro.local_settings import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from home.views import home

urlpatterns = [
    path('',home),
    path(ADMIN_URL, admin.site.urls),
    path('',include('user_panel.urls')),
    path('content/',include('content.urls'),name='content-url'),
    path('user_panel/',include('user_panel.urls'),name='user-panel-url'),
    # path('user_activity/',include('user_activity.urls'), name='user-activity-url'),
    path('logger/', include('logger.urls'),name='logger-url'),
    # SimpleJWT URLs
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api-auth/', include('rest_framework.urls')),
]

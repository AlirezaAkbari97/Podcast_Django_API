from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Profile, Channel


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('id','username', 'email', 'phone_number', 'is_staff')
    search_fields = ('username', 'email', 'phone_number')
    readonly_fields = ('date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


class FollowedChannelInline(admin.TabularInline):
    model = Profile.following_channels.through
    extra = 1


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id','user', 'description', 'profile_photo']
    # search_fields = ['user__username', 'bio', 'location']
    # list_filter = ['location']
    inlines = [FollowedChannelInline]


@admin.register(Channel)
class ChannelAdmin(admin.ModelAdmin):
    list_display = ['name','description','owner']

from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from .models import CustomUser, FollowedChannel, Profile, Channel


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'phone_number', 'password')

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password_confirm = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'password', 'password_confirm', 'email', 'phone_number')
        extra_kwargs = {
            'phone_number': {'required': False}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password_confirm']:
            raise serializers.ValidationError("Passwords do not match")
        return attrs

    def create(self, validated_data):
        validated_data.pop('password_confirm')
        return CustomUser.objects.create_user(**validated_data)


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=CustomUser.objects.none())
    class Meta:
        model = Profile
        fields = ['id','user', 'description', 'profile_photo']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].queryset = self.get_queryset()

    def get_queryset(self):
        # Retrieve the current user from the context
        user = self.context['request'].user
        return CustomUser.objects.filter(id=user.id)
        

class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = ('id', 'name', 'description', 'owner')

class FollowedChannelSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=CustomUser.objects.none())
    class Meta:
        model = FollowedChannel
        fields = ['id','user','channel','followed_at']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].queryset = self.get_queryset()

    def get_queryset(self):
        # Retrieve the current user from the context
        user = self.context['request'].user
        return CustomUser.objects.filter(id=user.id)
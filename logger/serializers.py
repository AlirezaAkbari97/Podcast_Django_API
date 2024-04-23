from rest_framework import serializers
from .models import ViewedContent, ViewedChannel


class ViewedContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ViewedContent
        fields = '__all__'


class ViewedChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ViewedChannel
        fields = '__all__'

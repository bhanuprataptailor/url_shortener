from rest_framework import serializers
from .models import CoreMapping


class CoreMappingSerializer(serializers.Serializer):

    class Meta:
        model = CoreMapping
        fields = ['short_url', 'long_url']

    id = serializers.IntegerField(read_only=True)
    counter = serializers.IntegerField(read_only=True)
    long_url = serializers.URLField(required=True)
    short_url = serializers.URLField(required=True)

    def create(self, validated_data):
        return CoreMapping.objects.create(**validated_data)

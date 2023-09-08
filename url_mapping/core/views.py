from django.shortcuts import render

# Create your views here.

from rest_framework.response import Response
from rest_framework.views import APIView
from .models import CoreMapping
from .serializers import CoreMappingSerializer
from rest_framework import status
from .jarvis.get_unique_key import generate_unique_key
from django.conf import settings


class ShortUrlView(APIView):

    def get_object(self, id):
        """
        Helper method to get the object with given todo_id, and user_id
        """
        try:
            short_url = settings.CORE_END_POINT + '/' + id
            return CoreMapping.objects.get(short_url=short_url)
        except CoreMapping.DoesNotExist:
            return None

    def get(self, request, pk, *args, **kwargs):

        instance = self.get_object(id=pk)
        serializer = CoreMappingSerializer(instance, many=False)
        return Response(serializer.data, status=status.HTTP_302_FOUND)


class CreateUrlView(APIView):
    def post(self, request, *args, **kwargs):
        key = generate_unique_key()
        long_url = self.request.data.get('long_url')
        if not long_url:
            return Response({"message": "long_url payload is required"}, 400)
        result = settings.CORE_END_POINT + '/' + key
        try:
            instance = CoreMapping.objects.get(long_url=long_url)
        except:
            instance = CoreMapping.objects.create(long_url=long_url, short_url=result)
            instance.save()
        return Response({"long_url": long_url, "short_url": result}, 201)

from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from API.serializers import EventSerializer
from API.models import Events


class OffersView(APIView):
    """
    GetByLocation post
    id, long, lat
    """

    def post(self, request, format=None):
        data = request.data
        resp = Events.objects.all()
        a = EventSerializer(resp, many=True).data
        return Response(a, status=status.HTTP_201_CREATED)

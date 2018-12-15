from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from API.search_logic.logic import find_by_category, find_by_location
from API.serializers import EventSerializer, LocationSerializer
from API.models import Events


class OffersView(APIView):
    """
    GetByCategory post
    id, long, lat
    """

    def post(self, request, format=None):
        data = request.data
        res = find_by_category(data['word'])
        a = EventSerializer(res, many=True).data
        return Response(a, status=status.HTTP_201_CREATED)

class LocationView(APIView):
    """
    GetByLocation post
    id, long, lat
    """

    def post(self, request, format=None):
        data = request.data
        resp = find_by_location(float(data['lat']), float(data['long']))
        a = LocationSerializer(resp, many=True).data
        return Response(a, status=status.HTTP_201_CREATED)
#olloi
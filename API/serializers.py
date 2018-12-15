from rest_framework import viewsets, serializers
from API.models import Events


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Events
        fields = '__all__'
        def create(self, validated_data):
            return Events.objects.create(**validated_data)

class LocationSerializer(serializers.ModelSerializer):
    length = serializers.SerializerMethodField()
    lat = serializers.SerializerMethodField()
    long = serializers.SerializerMethodField()

    def get_length(self, obj):
        return str(obj['length'])
    def get_lat(self, obj):
        return str(obj['lat'])
    def get_long(self, obj):
        return str(obj['long'])

    class Meta:
        model = Events
        fields = '__all__'
        def create(self, validated_data):
            return Events.objects.create(**validated_data)
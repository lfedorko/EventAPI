from rest_framework import viewsets, serializers
from API.models import Events


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Events
        fields = '__all__'
        def create(self, validated_data):
            return Events.objects.create(**validated_data)
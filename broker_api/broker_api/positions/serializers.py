from rest_framework import serializers
from .models import Position

class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = [
            'account',
            'underlying',
            'quantity',
            'cost'
        ]

    def create(self, validated_data):
        return Position.objects.create(**validated_data)

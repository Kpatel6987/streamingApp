from rest_framework import serializers
from .models import Account

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        positions = serializers.StringRelatedField(many=True)
        fields = [
            'user',
            'account_name',
            'positions',
            'buying_power',
            'initial_cash'
        ]
        extra_kwargs = {
            'buying_power': {'read_only': True},
            'positions': {'read_only': True}
        }

    def create(self, validated_data):
        return Account.objects.create(**validated_data)

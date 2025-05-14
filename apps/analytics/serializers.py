from rest_framework import serializers

class CryptoSerializer(serializers.Serializer):
    name = serializers.CharField()
    symbol = serializers.CharField()
    # price = serializers.FloatField()
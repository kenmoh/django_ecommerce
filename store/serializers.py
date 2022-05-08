from rest_framework import serializers


# noinspection PyAbstractClass
class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    unit_price = serializers.DecimalField(max_digits=8, decimal_places=2)
from decimal import Decimal
from rest_framework import serializers
from .models import Product


# noinspection PyAbstractClass,PyMethodMayBeStatic
class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    unit_price = serializers.DecimalField(max_digits=8, decimal_places=2)
    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')

    def calculate_tax(self, product: Product):
        return product.unit_price * Decimal(1.05)
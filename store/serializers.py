from decimal import Decimal
from rest_framework import serializers
from .models import Product


class CollectionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'unit_price', 'price_with_tax', 'collection']
    # id = serializers.IntegerField()
    # title = serializers.CharField(max_length=255)
    # price = serializers.DecimalField(max_digits=8, decimal_places=2, source='unit_price')
    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')
    # collection = serializers.StringRelatedField()
    # collection = serializers.PrimaryKeyRelatedField(queryset=Collection.objects.all())
    collection = CollectionSerializer()

    def calculate_tax(self, product: Product):
        return round(product.unit_price * Decimal(1.05), 2)

from decimal import Decimal
from rest_framework import serializers
from .models import Product, Collection, Review


# class CollectionSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=255)

class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'title', 'products_count']
    products_count = serializers.IntegerField(read_only=True)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'slug', 'inventory', 'unit_price', 'price_with_tax', 'collection', 'description']
    # id = serializers.IntegerField()
    # title = serializers.CharField(max_length=255)
    # price = serializers.DecimalField(max_digits=8, decimal_places=2, source='unit_price')
    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')
    collection = serializers.StringRelatedField()
    # collection = serializers.PrimaryKeyRelatedField(queryset=Collection.objects.all())
    # collection = CollectionSerializer()

    def calculate_tax(self, product: Product):
        return round(product.unit_price * Decimal(1.05), 2)


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        field = ['id', 'date', 'name', 'description', 'product']

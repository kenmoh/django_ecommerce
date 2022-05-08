from django.contrib import admin
from django.db.models import Count
from django.utils.html import format_html, urlencode
from django.urls import reverse
from .models import Collection, Product, Customer, Order


# noinspection PyMethodMayBeStatic
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'unit_price', 'inventory_status']
    list_editable = ['unit_price']
    list_per_page = 50

    # Computed Field
    @admin.display(ordering='inventory')
    def inventory_status(self, product):
        if product.inventory < 10:
            return 'Low'
        return 'OK'


# noinspection PyMethodMayBeStatic
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'membership', 'orders']
    list_editable = ['membership']
    ordering = ['first_name', 'last_name']
    list_per_page = 50

    def orders(self, customer):
        return customer.order_set.count()


# noinspection PyMethodMayBeStatic
@admin.register(Collection)
class CollectionAdin(admin.ModelAdmin):
    list_display = ['title', 'product_count']

    # Computed Field
    @admin.display(ordering='product_count')
    def product_count(self, collection):
        url = (reverse('admin:store_product_changelist')
               + '?'
               + urlencode({
                    'collection__id': str(collection.id)
                }))
        return format_html(f'<a href={url}>{collection.product_count}</a>')

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            product_count=Count('product')
        )


admin.site.register(Order)

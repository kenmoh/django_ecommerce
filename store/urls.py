from django.urls import path
from . import views

urlpatterns = [
    # path('products/', views.product_list),
    path('products/', views.ProductListView.as_view()),
    # path('products/<int:id>', views.product_detail),
    path('products/<int:id>', views.ProductDetailView.as_view()),
    path('collections/', views.collection_list),
    path('collections/<int:id>/', views.collection_details, name='collections')
]

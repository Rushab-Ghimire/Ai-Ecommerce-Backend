from django.urls import path
from .views import ProductListCreateView, ProductDetailView,CategoryListCreateView,CategoryDetailView,InventoryListView,InventoryDetailView

urlpatterns = [
    path('categories/', CategoryListCreateView.as_view(), name='category-list-create'),
    path('categories/<uuid:pk>', CategoryDetailView.as_view(), name='category-detail'),

    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<uuid:pk>/', ProductDetailView.as_view(), name='product-detail'),

    path('inventory/', InventoryListView.as_view(), name='inventory-list'),
    path('inventory/<uuid:pk>/', InventoryDetailView.as_view(), name='inventory-detail'),


]
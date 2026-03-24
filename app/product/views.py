from django.shortcuts import render
from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.exceptions import PermissionDenied
from .models import Product,Category, Inventory
from .serializers import ProductSerializer, CategorySerializer, InventorySerializer

# Create your views here.
class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'description']
    ordering_fields = ['name', 'created_at']

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_destroy(self, instance):
        instance.is_deleted =  True
        instance.save()


class ProductListCreateView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'description', 'category_name']
    ordering_fields = ['price', 'name', 'created_at']

    def get_queryset(self):
        return Product.objects.select_related('category').prefetch_related('inventory').all()
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Product.objects.select_related('category').prefetch_related('inventory').all()

    def perform_update(self, serializer):
        serializer.save(updated_at=None)

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()

class InventoryDetailView(generics.RetrieveUpdateAPIView):
    queryset = Inventory.objects.select_related('product').all()
    serializer_class = InventorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_permissions(self):
       if self.request.method in ['PUT', 'PATCH']:
           return [IsAdminUser()]
       return [IsAuthenticatedOrReadOnly()]
    
class InventoryListView(generics.ListAPIView):
    queryset = Inventory.objects.select_related('product').all()
    serializer_class = InventorySerializer
    permission_classes = [IsAdminUser]
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['stock', 'product__name', 'created_at']



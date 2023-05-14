from apps.base.api import GeneralListAPIView
from apps.products.api.serializers.product_serializers import ProductSerializer
from rest_framework import generics, viewsets, filters, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication
from apps.products.models import Product


class ProductListAPIView(GeneralListAPIView):
    serializer_class = ProductSerializer


class ProductCreateAPIView(generics.CreateAPIView):
    serializer_class = ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    authentication_classes = [BasicAuthentication]
    permission_classes = [permissions.AllowAny]
    queryset = Product.objects.all()
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['id', 'name']
    ordering_fields = ['id', 'name']
    ordering = ['id']
    serializer_class = ProductSerializer

from rest_framework import generics, viewsets
from apps.products.api.serializers.general_serializers import MeasureUnitSerializer, CategoryProductSerializer, IndicatorSerializer
# from apps.base.api import GeneralListAPIView
from rest_framework.authentication import BasicAuthentication
from rest_framework import generics, viewsets, filters, permissions
from apps.products.models import MeasureUnit, Indicator, CategoryProduct

'''
class MeasureUnitListAPIView(GeneralListAPIView):
    serializer_class = MeasureUnitSerializer
class IndicatorListAPIView(GeneralListAPIView):
    serializer_class = IndicatorSerializer
class CategoryProductListAPIView(GeneralListAPIView):
    serializer_class = CategoryProductSerializer
'''


class MeasureUnitViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]
    permission_classes = [permissions.AllowAny]
    queryset = MeasureUnit.objects.all()
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['id', 'description']
    ordering_fields = ['id', 'description']
    ordering = ['id']
    serializer_class = MeasureUnitSerializer


class IndicatorViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]
    permission_classes = [permissions.AllowAny]
    queryset = Indicator.objects.all()
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['id', 'description']
    ordering_fields = ['id', 'description']
    ordering = ['id']
    serializer_class = IndicatorSerializer


class CategoryProductViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]
    permission_classes = [permissions.AllowAny]
    queryset = CategoryProduct.objects.all()
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['id', 'description']
    ordering_fields = ['id', 'description']
    ordering = ['id']
    serializer_class = CategoryProductSerializer

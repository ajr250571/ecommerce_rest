from rest_framework import generics
from apps.products.api.serializers.general_serializers import MeasureUnitSerializer, CategoryProductSerializer, IndicatorSerializer
from apps.base.api import GeneralListAPIView


class MeasureUnitListAPIView(GeneralListAPIView):
    serializer_class = MeasureUnitSerializer


class IndicatorListAPIView(GeneralListAPIView):
    serializer_class = IndicatorSerializer


class CategoryProductListAPIView(GeneralListAPIView):
    serializer_class = CategoryProductSerializer

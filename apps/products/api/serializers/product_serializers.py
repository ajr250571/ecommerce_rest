from rest_framework import serializers
from apps.products.models import Product
from apps.products.api.serializers.general_serializers import MeasureUnitSerializer, CategoryProductSerializer


class ProductSerializer(serializers.ModelSerializer):
    # measure_unit = MeasureUnitSerializer()
    # measure_unit = serializers.StringRelatedField()

    # category_product = CategoryProductSerializer()
    # category_product = serializers.StringRelatedField()

    class Meta:
        model = Product
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date',)

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'name': instance.name,
            'description': instance.description,
            'image': instance.image if instance.image != '' else '',
            'measure_unit': instance.measure_unit.description,
            'category_product': instance.category_product.description
        }

    '''
    def update(self, instance, validated_data):
        updated_product = super().update(instance, validated_data)
        if 'image' in validated_data:
            instance.image = validated_data.get('image', instance.image)
        updated_product.save()
        return updated_product
    '''

from django.contrib import admin
from .models import MeasureUnit, CategoryProduct, Indicator, Product


class MeasureUnitAdmin(admin.ModelAdmin):
    list_display = ('id', 'description')
    ordering = ('id',)

class CategoryProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'description')
    ordering = ('id',)


admin.site.register(MeasureUnit, MeasureUnitAdmin)
admin.site.register(CategoryProduct, CategoryProductAdmin)
admin.site.register(Indicator)
admin.site.register(Product)

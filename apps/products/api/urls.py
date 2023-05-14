# from apps.products.api.views.general_views import CategoryProductListAPIView, IndicatorListAPIView
# from apps.products.api.views.product_views import ProductListAPIView, ProductCreateAPIView
from django.urls import path, include
from rest_framework import routers
from apps.products.api.views.product_views import ProductViewSet
from apps.products.api.views.general_views import MeasureUnitViewSet, CategoryProductViewSet, IndicatorViewSet

router = routers.DefaultRouter()
router.register('product', ProductViewSet, 'product')
router.register('measure_unit', MeasureUnitViewSet, 'measure_unit')
router.register('indicator', IndicatorViewSet, 'indicator')
router.register('category_product', CategoryProductViewSet, 'category_product')


urlpatterns = [
    path('', include(router.urls)),

    # path("measure_unit/", MeasureUnitListAPIView.as_view(), name="measure_unit"),
    # path("category_product/", CategoryProductListAPIView.as_view(),name="category_product"),
    # path("indicator/", IndicatorListAPIView.as_view(), name="indicator"),
    # path("product/list/", ProductListAPIView.as_view(), name="product_list"),
    # path("product/create/", ProductCreateAPIView.as_view(), name="product_create"),
]

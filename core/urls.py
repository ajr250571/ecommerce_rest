from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api_users/', include('apps.users.api.urls')),
    path('api_products/', include('apps.products.api.urls')),
]

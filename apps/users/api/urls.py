from apps.users.api.api import UserViewSet, UserAPIView, user_api_view, LogoutView, LoginView
from rest_framework import routers
from django.urls import path, include

'''
urlpatterns = [
    path('users/', user_api_view, name='users'),
]
'''

'''
urlpatterns = [
    path('users/', UserAPIView.as_view(), name='users'),
]
'''

router = routers.DefaultRouter()
router.register('users', UserViewSet, 'users')

urlpatterns = [
    path('', include(router.urls)),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    ]

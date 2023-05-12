from rest_framework.response import Response
from rest_framework.views import APIView
from apps.users.models import User
from apps.users.api.serializers import UserSerializer
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import api_view
from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from rest_framework import serializers, filters, authentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from django.contrib.auth import logout, login, authenticate


class CustomBasicAuthentication(BasicAuthentication):
    def authenticate_credentials(self, userid, password, request=None):
        user = authenticate(request, username=userid, password=password)
        if user is None:
            return None
        return (user, None)


class LoginView(APIView):
    authentication_classes = [CustomBasicAuthentication]

    def post(self, request):
        user = request.user
        if user.is_authenticated:
            login(request, user)
            return Response({'detail': 'Logged in'}, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response({'detail': 'Logged out'}, status=status.HTTP_200_OK)


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [BasicAuthentication]
    queryset = User.objects.all()
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['username', 'name', 'last_name']
    ordering_fields = ['id', 'username', 'last_name']
    ordering = ['id']
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        # Aquí puedes agregar tu lógica personalizada antes de guardar el objeto
        # Por ejemplo, puedes modificar los datos validados antes de guardarlos
        
        '''
        password = serializer.validated_data.get('password')
        try:
            validate_password(password)
        except ValidationError as e:
            # Capturar la excepción ValidationError y manejar el error
            # Por ejemplo, puedes generar una excepción serializers.ValidationError para mostrar el error al usuario
            raise serializers.ValidationError({'password': e.messages})

        password_encriptada = make_password(password)
        serializer.validated_data['password'] = password_encriptada
        # Luego llamas al método save() del serializador para guardar el objet
        '''
        serializer.save()


@api_view(['GET', 'POST'])
def user_api_view(request):
    if request.method == 'GET':
        users = User.objects.all()
        users_serializer = UserSerializer(users, many=True)
        return Response(users_serializer.data)

    if request.method == 'POST':
        user_serializer = UserSerializer(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data, status=status.HTTP_201_CREATED)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserAPIView(APIView):
    def get(self, request, format=None):
        users = User.objects.all()
        users_serializer = UserSerializer(users, many=True)
        return Response(users_serializer.data)

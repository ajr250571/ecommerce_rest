from rest_framework import serializers
from apps.users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'last_name', 'name', 'email', 'password',)
        # '__all__'
        # ('id', 'username', 'last_name', 'name', 'email', 'password',)

    # VALIDATES
    def validate_username(self, value):
        value = value.strip()
        return value

    def validate_name(self, value):
        if 'developer' in value.strip():
            raise serializers.ValidationError(
                'Error, no puede existir usuario con ese nombre.')
        return value.strip()

    def validate_last_name(self, value):
        return value

    def validate_email(self, value):
        username = self.validate_name(self.initial_data.get('username'))
        if username.upper() in value.upper():
            raise serializers.ValidationError(
                'Error, el Username no puede estar en el email.')
        return value

    # VALIDA LOS DATOS DE ENTRADA
    def validate(self, data):
        # Ejemplo: data['name']
        return data

    # SALIDA DE DATOS
    def to_representation(self, instance):
        # Aquí puedes personalizar cómo se representan los datos de salida
        # Por ejemplo, puedes mostrar solo algunos campos en la salida
        # data = super().to_representation(instance)
        # data['campo1'] = data['campo1'] + 1
        data = {
            'id': instance.id,
            'username': instance.username,
            'last_name': instance.last_name,
            'name': instance.name,
            'email': instance.email,
        }
        return data

    # POST
    def create(self, validated_data):
        # validated_data['name'] = validated_data['name']
        # print(validated_data)
        # return super().create(validated_data)
        # return User.objects.create(**validated_data)

        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    # PUT
    def update(self, instance, validated_data):
        '''
        user = User(**validated_data)
        user.save()
        return user
        '''
        '''
        updated_user = super().update(instance, validated_data)
        updated_user.set_password(validated_data['password'])
        updated_user.save()
        return updated_user
        '''
        instance.username = validated_data.get('username', instance.username)
        instance.last_name = validated_data.get(
            'last_name', instance.last_name)
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance

    # PATCH

    def partial_update(self, instance, validated_data):
        '''
        instance.username = validated_data.get('username', instance.username)
        instance.last_name = validated_data.get(
            'last_name', instance.last_name)
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance
        '''
        updated_user = super().update(instance, validated_data)
        if 'password' in validated_data:
            updated_user.set_password(validated_data['password'])
        updated_user.save()
        return updated_user

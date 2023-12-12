from rest_framework import serializers
from django.core import exceptions
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import get_user_model
User = get_user_model()


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'full_name', 'phone','password')

    # this validate function is cheking password if its a proper one.
    def validate(self,data):
        user = User(**data)
        password = data.get('password')
        try:
            validate_password(password,user)
        except exceptions.ValidationError as e:
            serializer_errors = serializers.as_serializer_error(e)
            raise exceptions.ValidationError(
                {'password' : serializer_errors['non_field_errors']}
            )

        return data

    def create(self, validated_data):
        user = User.objects.create_user(
            username = validated_data['username'],
            email = validated_data['email'],
            full_name = validated_data['full_name'],
            phone = validated_data['phone'],
            password = validated_data['password'],
        )

        return user
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username', 'email', 'full_name', 'phone','profile_image','is_superuser','last_login','is_admin','is_staff','is_active')

class ProfilePictureUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['profile_image'] 



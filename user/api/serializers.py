from rest_framework import serializers
from user.models import User


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'phone', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def save(self):
        account = User(
            phone=self.validated_data['phone'],
            email=self.validated_data['email'],
            username=self.validated_data['username'],

        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({'password': 'Пароли должны совпадать!'})
        account.set_password(password)
        account.save()
        return account



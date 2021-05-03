from rest_framework import serializers
from accounts.models import CustomUser
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustomUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'event','username')


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, CustomUser):
        token = super(MyTokenObtainPairSerializer, cls).get_token(CustomUser)

        # Add custom claims
        token['username'] = CustomUser.username
        # token['password'] = user.password
        return token
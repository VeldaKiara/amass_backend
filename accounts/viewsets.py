from rest_framework import viewsets
from .models import CustomUser
from .serializers import CustomUserSerializer, MyTokenObtainPairSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken


class CustomUserViewsSets(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    # permission_classes = [IsAuthenticated]

    @classmethod
    def get_token(cls, user):
        return RefreshToken.for_user(user)

    # This overrides the default user creation behaviour to return a valid token instead of a user instance
    def create(self, request):
        s = CustomUserSerializer(data=request.data)
        if s.is_valid():
            data = {}
            user = s.save()
            refresh = self.get_token(user)

            data['refresh'] = str(refresh)
            data['access'] = str(refresh.access_token)
            return Response(data)

        return Response(s.errors)


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer

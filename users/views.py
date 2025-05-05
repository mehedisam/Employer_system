from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import SignUpSerializer, UserSerializer

User = get_user_model()

class SignUpView(generics.CreateAPIView):
    """POST /api/auth/signup/"""
    serializer_class = SignUpSerializer
    permission_classes = [AllowAny]

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = 'email'  # use email instead of username:contentReference[oaicite:19]{index=19}

class CustomTokenObtainPairView(TokenObtainPairView):
    """POST /api/auth/login/"""
    serializer_class = CustomTokenObtainPairSerializer

class ProfileView(generics.RetrieveAPIView):
    """GET /api/auth/profile/"""
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

class LogoutView(generics.GenericAPIView):
    """POST /api/auth/logout/ (blacklist refresh token)"""
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data.get("refresh")
            token = RefreshToken(refresh_token)
            token.blacklist()  # blacklist the refresh token:contentReference[oaicite:20]{index=20}
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)

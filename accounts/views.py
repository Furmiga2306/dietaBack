from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenObtainPairSerializer

class CustomTokenObtainPairView(TokenObtainPairView):
    """
    View personalizada para obter o token JWT com base no email.
    """
    serializer_class = CustomTokenObtainPairSerializer

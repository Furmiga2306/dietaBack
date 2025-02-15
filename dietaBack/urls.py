"""
URL configuration for dietaBack project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,  # Para obter o token (login)
    TokenRefreshView,  # Para atualizar o token
    TokenVerifyView,  # Para verificar o token
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),  # Rotas do Djoser para cadastro
    path('auth/jwt/create/', TokenObtainPairView.as_view(), name='jwt-create'),  # Login (obter token)
    path('auth/jwt/refresh/', TokenRefreshView.as_view(), name='jwt-refresh'),  # Atualizar token
    path('auth/jwt/verify/', TokenVerifyView.as_view(), name='jwt-verify'),  # Verificar token
]

from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import User

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    Serializer para obter o token JWT com base no email (não username).
    """
    
    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        # Verifica se os dados de email e senha estão corretos
        if email and password:
            try:
                # Tenta buscar o usuário pelo email
                user = User.objects.get(email=email)
                if user.check_password(password):
                    # Se a senha estiver correta, gera os tokens
                    return super().validate(attrs)
                else:
                    raise serializers.ValidationError("Senha incorreta")
            except User.DoesNotExist:
                raise serializers.ValidationError("Usuário não encontrado")

        raise serializers.ValidationError("Email e senha são necessários")


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'gender']
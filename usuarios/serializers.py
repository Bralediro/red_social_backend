from rest_framework import serializers
from .models import Categorias, Usuarios, Recover, Level, Paises, Sentimental, Profile

class CategoriasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorias
        fields = "__all__"

class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields = "__all__"

class RecoverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recover
        fields = "__all__"

class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = "__all__"

class PaisesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paises
        fields = "__all__"

class SentimentalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sentimental
        fields = "__all__"

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"
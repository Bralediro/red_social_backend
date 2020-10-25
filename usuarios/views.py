
from rest_framework import viewsets
from .serializers import CategoriasSerializer, Categorias, Usuarios, UsuariosSerializer, Recover, RecoverSerializer, Level, LevelSerializer, Paises, PaisesSerializer, Sentimental, SentimentalSerializer, Profile, ProfileSerializer


# Create your views here.

class CategoriasView(viewsets.ModelViewSet):
    queryset = Categorias.objects.all()
    serializer_class = CategoriasSerializer

class UsuariosView(viewsets.ModelViewSet):
    queryset = Usuarios.objects.all()
    serializer_class = UsuariosSerializer

class RecoverView(viewsets.ModelViewSet):
    queryset = Recover.objects.all()
    serializer_class = RecoverSerializer

class LevelView(viewsets.ModelViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer

class PaisesView(viewsets.ModelViewSet):
    queryset = Paises.objects.all()
    serializer_class = PaisesSerializer

class SentimentalView(viewsets.ModelViewSet):
    queryset = Sentimental.objects.all()
    serializer_class = SentimentalSerializer

class ProfileView(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
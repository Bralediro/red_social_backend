
from rest_framework import viewsets
from .serializers import CategoriasSerializer, Categorias, Usuarios, UsuariosSerializer, Recover, RecoverSerializer, Level, LevelSerializer, Paises, PaisesSerializer, Sentimental, SentimentalSerializer, Profile, ProfileSerializer, Album, AlbumSerializer, Imagen, ImagenSerializer, Post, PostSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class CurrentUser(viewsets.ModelViewSet):
    def get_queryset(self):
        user = self.request.user
        return self.serializer_class.Meta.model.objects.filter(usuario=user)

    
class CategoriasView(viewsets.ModelViewSet):
    queryset = Categorias.objects.all()
    serializer_class = CategoriasSerializer

class UsuariosView(CurrentUser):
    queryset = Usuarios.objects.all()
    serializer_class = UsuariosSerializer
    permissions_classes = [IsAuthenticated]
    
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

class ProfileView(CurrentUser):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    #permissions_classes = [IsAuthenticated]
    
class AlbumView(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class ImagenView(viewsets.ModelViewSet):
    queryset = Imagen.objects.all()
    serializer_class = ImagenSerializer

class PostView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
from django.urls import path
from .views import CategoriasView, UsuariosView, RecoverView, LevelView, PaisesView, SentimentalView, ProfileView,AlbumView, ImagenView, PostView

urlpatterns = [
    path('categorias/', CategoriasView.as_view({
        'get': 'list',
        'post': 'create'
        
    })),
    path('categorias/<int:pk>', CategoriasView.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    path('usuarios/', UsuariosView.as_view({
        'get': 'list',
        'post': 'create'
        
    })),
    path('usuarios/<int:pk>', UsuariosView.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    path('recover/', RecoverView.as_view({
        'get': 'list',
        'post': 'create'
        
    })),
    path('recover/<int:pk>', RecoverView.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    path('level/', LevelView.as_view({
        'get': 'list',
        'post': 'create'        
    })),
    path('paises/', PaisesView.as_view({
        'get': 'list',
        'post': 'create'        
    })),
    path('sentimental/', SentimentalView.as_view({
        'get': 'list',
        'post': 'create'        
    })),
    path('profile/', ProfileView.as_view({
        'get': 'list',
        'post': 'create'        
    })),
    path('profile/<int:pk>', ProfileView.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    path('album/', AlbumView.as_view({
        'get': 'list',
        'post': 'create'        
    })),
    path('album/<int:pk>', AlbumView.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    path('imagen/', ImagenView.as_view({
        'get': 'list',
        'post': 'create'        
    })),
    path('imagen/<int:pk>', ImagenView.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    path('post/', PostView.as_view({
        'get': 'list',
        'post': 'create'        
    })),
    path('post/<int:pk>', PostView.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),

]

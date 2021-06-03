from django.urls import path
from . import views
from .views import *

urlpatterns = [
  path('', IndexView.as_view(), name='index'),
  path('cadastrar/cliente', ClienteCreate.as_view(), name='cadastrar-cliente'),
  path('cadastrar/livro', LivroCreate.as_view(), name='cadastrar-livro'),
  path('listar/livros', LivroList.as_view(), name='listar-livros'),
]

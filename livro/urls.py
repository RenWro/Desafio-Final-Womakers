from django.urls import path
from .views import listar_livros, detalhe_livro, search_view
from . import views
from django.http import HttpResponse
from django.conf import settings
from django.conf.urls.static import static

app_name = 'Livros'

urlpatterns = [
    path('', views.listar_livros),
    path('detalhe_livro/<int:id>/', views.detalhe_livro),
    path('adicionar-ao-carrinho/', views.adicionar_ao_carrinho, name='adicionar_ao_carrinho'),
    path('search/', views.search_view, name='search'),
]

if settings.DEBUG: urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
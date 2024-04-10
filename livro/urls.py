from django.urls import path
from .views import listar_livros, detalhe_livro
from . import views
from django.http import HttpResponse
from django.conf import settings
from django.conf.urls.static import static

app_name = 'Livros'

urlpatterns = [
    path('', listar_livros),
    path('detalhe_livro/<int:id>/', detalhe_livro),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

"""
URL configuration for livraria project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from livro.views import listar_livros
from pagamento import urls as pagamento_urls  # Renomeado para uma nomenclatura mais genérica

urlpatterns = [
    path('', listar_livros),
    path('admin/', admin.site.urls),
    path('cliente/', include('cliente.urls', namespace='cliente')),
    path('pedido/', include('pedidos.urls', namespace='pedidos')),
    # path('pagamento/', include(pagamento_urls)),
    path('', include('paypal.standard.ipn.urls')),
]


# urlpatterns = [
#     path('', main),
#     path('admin/', admin.site.urls),
#     path('livros/', include('app.urls')),
#     path('cliente/', include('cliente.urls', namespace='cliente')),
#     path('paypal', include('paypal.standard.ipn.urls')),
#     path('pagamento/', include('pagamento.urls', namespace='pagamento')),
#     path('paypal', include('paypal.standard.ipn.urls')),
#     path('pagamento/', include('pagamento.urls', namespace='pagamento')),
# ]

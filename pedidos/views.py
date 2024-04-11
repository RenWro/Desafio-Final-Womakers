from django.shortcuts import render, get_object_or_404, redirect
from pedidos.models import Pedido, Carrinho
from livro.models import Livro
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
# PRIMEIRO CARRINHO DEPOIS PEDIDOS

# CARRINHO


def ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


@login_required
def detalhes_carrinho(request):
    cliente = request.user
    detalhes_do_carrinho = 'Seu carrinho ainda está vazio.'
    carrinho_vazio = True
    if Carrinho.objects.filter(cliente=cliente).exists():
        carrinho_do_usuario = Carrinho.objects.filter(cliente=cliente).last()
        detalhes_do_carrinho = carrinho_do_usuario.ver_detalhes()
        carrinho_vazio = False

    context = {
        'carrinho_vazio': carrinho_vazio,
        'carrinho': detalhes_do_carrinho,
        'cliente': cliente
    }
    return render(request, 'detalhes_carrinho.html', context)


def atualizar_carrinho(request):
    livro_id = request.POST.get('livro_id')
    if livro_id is not None:
        try:
            item_livro = Livro.objects.get(id=livro_id)
        except Livro.DoesNotExist:
            print("Esse livro acabou!")
            return redirect("home.html")
        item_carr, novo_item = Carrinho.objects.novo_ou_existente(request)
        if item_livro in item_carr.livros.all():
            item_carr.livros.remove(item_livro)
            adicionar = False
        else:
            item_carr.livros.add(item_livro)
            adicionar = True
        # login do usuário, talvez tenha q alterar
        request.session['cart_items'] = item_carr.livros.count()
        if ajax(request):
            print("Ajax request")
            json_data = {
                "adicionar": adicionar,
                "remover": not adicionar,
                "contagemLivros": item_carr.livros.count()
            }
            return JsonResponse(json_data)
            # return JsonResponse({"message": "Erro 400"}, status = 400)
    return redirect("/")


# PEDIDOS

def listar_pedidos_cliente(request, cliente_id):
    # Filtra os pedidos do cliente e os ordena por data, da mais recente para a mais antiga
    pedidos = Pedido.objects.filter(
        cliente_id=cliente_id).order_by('-data_pedido')
    return render(request, 'listar_pedidos_cliente.html', {'pedidos': pedidos})


def detalhar_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, pk=pedido_id)
    return render(request, 'detalhes_pedido.html', {'pedido': pedido})


def finalizar_pedido(request, cliente_id):
    '''
    Aqui vai ser criado um pedido de fato?

    Pegar todos os dados do SPAN???

    '''
    if request.method == 'POST':
        formulario = Pedido(request.POST)
        if formulario.is_valid():
            # Crie um objeto Pedido com os dados do formulário e o ID do cliente
            pedido = formulario.save(commit=False)
            pedido.cliente_id = cliente_id  # Associar o pedido ao cliente específico
            pedido.save()
            # PEDIDO CONCLUÍDO COM SUCESSO
            # Redirecionar para a página de sucesso
            return redirect('pagina_de_sucesso')
    else:
        formulario = Pedido()

    return render(request, 'detalhes_pedido.html', {'formulario': formulario})


'''
CRIAR LÓGICA DO CARRINHO PRA FICAR NO SPAM

# models.py
from django.db import models
from django.contrib.auth.models import User

class Carrinho(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    # Outros campos, como data de criação, podem ser adicionados conforme necessário

class ItemCarrinho(models.Model):
    carrinho = models.ForeignKey(Carrinho, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField(default=1)
    # Outros campos, como preço unitário, podem ser adicionados conforme necessário

    
# views.py
from django.shortcuts import render, redirect
from .models import Carrinho, ItemCarrinho

def adicionar_item_carrinho(request, produto_id):
    # Lógica para adicionar um item ao carrinho
    # Verifica se o usuário tem um carrinho existente na sessão
    # Adiciona o produto ao carrinho existente ou cria um novo carrinho se necessário
    return redirect('pagina_do_carrinho')

def visualizar_carrinho(request):
    # Lógica para visualizar o carrinho
    # Recupera as informações do carrinho da sessão e renderiza um template com essas informações
    return render(request, 'carrinho.html', context)

def finalizar_compra(request):
    # Lógica para finalizar a compra
    # Recupera as informações do carrinho da sessão
    # Cria um objeto de pedido com base nessas informações
    # Limpa as informações do carrinho da sessão
    return render(request, 'compra_concluida.html')

def remover_item_carrinho(request, item_id):
    # Verifica se o usuário está autenticado
    if not request.user.is_authenticated:
        return redirect('login')  # Redireciona para a página de login se o usuário não estiver autenticado

    # Recupera o item do carrinho pelo seu ID
    item_carrinho = get_object_or_404(ItemCarrinho, pk=item_id)

    # Verifica se o item pertence ao carrinho do usuário atual
    if item_carrinho.carrinho.usuario != request.user:
        return redirect('pagina_do_carrinho')  # Redireciona para o carrinho se o item não pertencer ao usuário atual

    # Remove o item do carrinho
    item_carrinho.delete()

    return redirect('pagina_do_carrinho')



'''

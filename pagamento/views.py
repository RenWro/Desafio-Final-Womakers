from django.shortcuts import render
from pedidos.models import Pedido
from paypal.standard.forms import PayPalPaymentsForm
from django.conf import settings
import uuid # pra gerar um cod único
from django.urls import reverse

# # Create your views here.

def CheckOut(request, id):

    pedido = Pedido.objects.get(id=id) # será id = pedido_id?

    host = request.get_host()

    paypal_checkout = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': pedido.calcular_valor_total(),
        'item_name': pedido.id, # testar se preciso converter p str
        'invoice': uuid.uuid4(), # gerar um código único pra cada transação (rastreamento)
        'currency_code': 'BRL', # moeda R$
        'notify_url': f"http://{host}{reverse('paypal-ipn')}", # tá biblioteca do paypal instalada
        'return_url': f"http://{host}{reverse('payment-success', kwargs = {'id': id})}",
        'cancel_url': f"http://{host}{reverse('payment-failed', kwargs = {'id': id})}",
    }

    paypal_payment = PayPalPaymentsForm(initial=paypal_checkout)

    context = {
        'pedido': pedido,
        'paypal': paypal_payment
    }

    return render(request,'checkout.html', context)

def PaymentSuccessful(request, id): # verificar se é pedido_id

    pedido = Pedido.objects.get(id=id)
    
    return render(request, 'payment-success.html', {'pedido': pedido})


def PaymentFailed(request, id):

    pedido = Pedido.objects.get(id=id)
    
    return render(request, 'payment-failed.html', {'pedido': pedido})
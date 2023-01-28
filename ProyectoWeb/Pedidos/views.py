from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import LineaPedido, Pedidos
from django.contrib import messages
from Carro.Carro import Carro
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail

@login_required(login_url="/Autenticacion/Login")
def procesar_pedido(request):
    pedido =  Pedidos.objects.create(User=request.user)
    carro = Carro(request)
    lista_pedido = list()
    for key,value in carro.carro.items():
        lista_pedido.append(LineaPedido(
            producto_id= key,
            Cantidad= value['cantidad'],
            User=request.user,
            pedido=pedido    

        ))
    LineaPedido.objects.bulk_create(lista_pedido)
    Enviar_Mail(
        pedido=pedido,
        lista_pedido=lista_pedido,
        usuario = request.user.username,
        email_usuario= request.user.email

    )
    messages.success(request,'Se ha realizado con exito')
    return redirect('../Tienda')


def Enviar_Mail(**kwargs):
    Asunto =" Gracias por el pedido"
    mensage = render_to_string("Emails/Pedido.html",{
        "pedido": kwargs.get("pedido"),
        "lista_pedido":kwargs.get("lista_pedido"),
        "usuario":kwargs.get("usuario")
    })
    mensaje_texto= strip_tags(mensage)
    from_email='jmedinaguerrero847@gmail.com'
    #to= kwargs.get("email_usuario")
    to= "jmedinaguerrero847@gmail.com"
    send_mail(Asunto,mensaje_texto,from_email,[to],html_message=mensage)
# Create your views here.
 
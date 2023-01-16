from django.shortcuts import render,redirect
from .forms import FormularioContacto
from django.core.mail import EmailMessage
from  ProyectoWeb.settings import EMAIL_HOST_USER   


def Contactos(request):
    Formulario = FormularioContacto()
    
    if request.method =="POST":
        Formulario= FormularioContacto(data=request.POST)
        
        if Formulario.is_valid():
            nombre=request.POST.get("nombre")
            Email=request.POST.get("Email")
            Contenido=request.POST.get("Contenido")
            Email = EmailMessage("Mensaje desde Django", 
            "El usuario con nombre {} con  la direccion {} escribe lo siguiente: \n {}".format(nombre,Email,Contenido),
            "",[EMAIL_HOST_USER,], reply_to=[Email])
            try: 
                Email.send()
                return redirect("/Contacto/?valido")
            except:
                return redirect("/Contacto/?Eror")
            


    return render(request,"Contacto/contactos.html",{ "Formulario":Formulario })
# Create your views here.

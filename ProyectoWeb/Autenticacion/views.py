from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib import messages
class registro(View):
    def get(self,request):
        form=UserCreationForm()
        return render(request,'Autenticacion/Prueba.html',{'form':form})

    def post(self,request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            Usuario = form.save()
            login (request,Usuario)
            return redirect('Home')
        else:
            for msg in form.error_messages:
                messages.error(request,form.error_messages[msg])
            return render(request,'Autenticacion/Prueba.html',{'form':form})

def cerrar_sesion(request):
    logout(request)
    return redirect('Home')

def loguearse(request):

    if request.method== "POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre_usuario=form.cleaned_data.get("username")
            contra=form.cleaned_data.get("password")
            usuario=authenticate(username=nombre_usuario, password=contra)
            if usuario is not None:
                login(request,usuario)
                return redirect('Home')
            else: 
                messages.error(request,"Eror")

        else:
            messages.error(request,"Eror")
            
    form = AuthenticationForm()
    return render(request,'login/Logear.html',{'form':form})
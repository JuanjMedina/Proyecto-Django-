from django.shortcuts import render
from .models import Post, Categoria

def Blog(request):
    Post_disponibles = Post.objects.all()
    return render(request, "Blog/Blogs.html",{'Post':Post_disponibles})



def Categorias(request, categoria_id):
    Categoria_disponible = Categoria.objects.get(id=categoria_id)
    Post_Dispobibles = Post.objects.filter(Categorias=Categoria_disponible)
    return render(request, "Blog/Categoria.html",{'Categoria':Categoria,'Post':Post_Dispobibles})
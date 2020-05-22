from django.shortcuts import render, get_object_or_404
from django.utils import timezone #Para poder ordenar los datos por fecha
from .models import Post #Para poder usar los objetos post de la db


def post_list(request, *args, **kwargs):
    #La línea siguiente filtra los objetos Post recibidos por fecha de publicación
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):  #Pk es la clave primaria, la base de datos asigna una a cada post
    post = get_object_or_404(Post, pk=pk) #Si no existe el objeto regresa error 404
    return render(request, 'blog/post_detail.html', {'post': post})

from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone #Para poder ordenar los datos por fecha
from .models import Post #Para poder usar los objetos post de la db
from .forms import PostForm


def post_list(request, *args, **kwargs):
    #La línea siguiente filtra los objetos Post recibidos por fecha de publicación
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):  #Pk es la clave primaria, la base de datos asigna una a cada post
    post = get_object_or_404(Post, pk=pk) #Si no existe el objeto regresa error 404
    return render(request, 'blog/post_detail.html', {'post': post})


def post_new(request):
    #Si al momento de ir al servidor/post/new/ mandamos una petición del tipo post:
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
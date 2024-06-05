from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from blog.models import Post
from blog.forms import PostForm

"""
Views para o aplicativo de blog.

Este módulo contém as views utilizadas no aplicativo de blog, 
incluindo listagem, detalhes, criação e edição de posts.
"""

# Create your views here.
def post_list(request):
    """
    View para listar os posts publicados.

    Args:
        request (HttpRequest): O objeto de requisição HTTP.

    Returns:
        HttpResponse: A resposta HTTP com a renderização da template
        'post_list.html' e o contexto contendo os posts em 
        ordem temporária.
    """

    posts = Post.objects.filter(
        published_date__lte = timezone.now()).order_by('published_date').reverse
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    """
    View para exibir os detalhes de um post específico.

    Args:
        request (HttpRequest): O objeto de requisição HTTP.
        pk (int): A chave primária do post a ser exibido.

    Returns:
        HttpResponse: A resposta HTTP com a renderização da template
        'post_detail.html' e o contexto contendo o post.
    """

    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    """
    View para criar um novo post.

    Args:
        request (HttpRequest): O objeto de requisição HTTP.

    Returns:
        HttpResponse: A resposta HTTP com a renderização da template
        'post_edit.html' e o contexto contendo o formulário.
    """

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
    """
    View para editar um post existente.

    Args:
        request (HttpRequest): O objeto de requisição HTTP.
        pk (int): A chave primária do post a ser editado.

    Returns:
        HttpResponse: A resposta HTTP com a renderização da template
        'post_edit.html' e o contexto contendo o formulário.
    """

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
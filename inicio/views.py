from inspect import signature
from pyexpat.errors import messages
from .models import Comment
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.db.models import Q
from .models import Post, Category, Entry
from .forms import PostForm, CommentForm
from .models import Article, Author
from django.contrib.auth import authenticate, login


def index(request):
    posts = Post.objects.all()
    return render(request, 'inicio/index.html')

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', slug=post.slug)
    else:
        form = PostForm()
    return render(request, 'inicio/create_post.html', {'form': form})

@login_required
def edit_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', slug=post.slug)
    else:
        form = PostForm(instance=post)
    return render(request, 'inicio/edit_post.html', {'form': form})

@login_required
def post_detail(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)
    comments = Comment.objects.filter(post=post)

    context = {
        'post': post,
        'comments': comments,
        'user': request.user,  # Asegurando que el contexto del usuario esté disponible
    }

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post_detail', post_slug=post.slug)
    else:
        form = CommentForm()

    context['form'] = form
    return render(request, 'inicio/post_detail.html', context)

def home_view(request):
    return render(request, 'inicio/home.html')


def blog_home(request):
    blog_posts = Post.objects.all()
    return render(request, 'inicio/blog_home.html', {'blog_posts': blog_posts})

def buscar_view(request):
    query = request.GET.get('q')
    resultados_tu_modelo2 = Post.objects.filter(Q(campo__icontains=query))  
    return render(request, 'buscar_resultados.html', {'resultados': resultados_tu_modelo2})

def signup_view_cuentas(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('index')  # Corregir la redirección según tu configuración
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')

    return render(request, 'inicio/login.html')

def search_posts(request):
    query = request.GET.get('q')
    if query:
        inicio_posts = Post.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        )
        blog_posts = Post.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        )
        posts = list(inicio_posts) + list(blog_posts)
    else:
        posts = []
    return render(request, 'search_results.html', {'posts': posts, 'query': query})


def add_post(request):
    # Aquí iría la lógica para procesar la solicitud de agregar un nuevo post
    return HttpResponse("Placeholder para agregar un nuevo post")


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'inicio/post_list.html', {'posts': posts})

def category_view(request, category_name):
    category = get_object_or_404(Category, name__iexact=category_name)
    posts = Post.objects.filter(categories=category)
    entries = Entry.objects.filter(category__name=category)
    return render(request, 'category.html', {'category': category.capitalize(), 'entries': entries})

def category_posts(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    posts = Post.objects.filter(category=category)
    return render(request, 'inicio/category_posts.html', {'category': category, 'posts': posts})

def category_cosmetica(request):
    posts = Post.objects.filter(category='cosmetica')
    return render(request, 'inicio/category_cosmetica.html', {'posts': posts})

def category_maquillaje(request):
    posts = Post.objects.filter(category='maquillaje')
    return render(request, 'inicio/category_maquillaje.html', {'posts': posts})

def category_dermocosmetica(request):
    posts = Post.objects.filter(category='dermocosmetica')
    return render(request, 'inicio/category_dermocosmetica.html', {'posts': posts})

def category_perfumeria(request):
    posts = Post.objects.filter(category='perfumeria')
    return render(request, 'inicio/category_perfumeria.html', {'posts': posts})

def category_formaciones(request):
    posts = Post.objects.filter(category='formaciones')
    return render(request, 'inicio/category_formaciones.html', {'posts': posts})

def category_contacto(request):
    posts = Post.objects.filter(category='contacto')
    return render(request, 'inicio/category_contacto.html', {'posts': posts})

def zoom_view(request):
    return render(request, 'inicio/zoom.html')

def generate_signature(request):
    # Lógica para generar la firma
    return JsonResponse({'signature': signature})

def cosmetica_view(request):
    category_cosmetica = get_object_or_404(Category, name__iexact='Cosmética')
    entries = Post.objects.filter(category=category_cosmetica)
    
    return render(request, 'inicio/cosmetica.html', {'posts': entries})

def maquillaje_view(request):
    category_maquillaje = get_object_or_404(Category, name__iexact='Maquillaje')
    entries = Post.objects.filter(category=category_maquillaje)
    
    return render(request, 'inicio/maquillaje.html', {'posts': entries})

def dermocosmetica_view(request):
    return render(request, 'inicio/dermocosmetica.html')

def perfumeria_view(request):
    # Obtén el objeto Category correspondiente a 'Perfumería'
    category_perfumeria = get_object_or_404(Category, name__iexact='Perfumería')
    
    # Filtra los posts que tienen esta categoría
    entries = Post.objects.filter(category=category_perfumeria)
    
    return render(request, 'inicio/perfumeria.html', {'posts': entries})

def formaciones_view(request):
    return render(request, 'inicio/formaciones.html')

def bienestar_view(request):
    return render(request, 'inicio/bienestar.html')

def contacto_view(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirigir a una página de éxito o a la misma página sin incluir los comentarios
            return redirect('contacto_success')  
    else:
        form = CommentForm()
    
    context = {
        'form': form,
    }
    
    return render(request, 'inicio/contacto.html', context)

def comment_success_view(request):
    return render(request, 'inicio/comment_success.html')

def mantenimiento_view(request):
    return render(request, 'inicio/mantenimiento.html')

def about_view(request):
    return render(request, 'inicio/about.html')

def article(request, pk):
    article = Article.objects.get(pk=pk)  # Ejemplo de obtención de un artículo por su clave primaria
    return render(request, 'inicio/article_detail.html', {'article': article})

def author_view(request, id):
    author = Author.objects.get(id=id)  # Ejemplo de obtención de un autor por su ID
    return render(request, 'inicio/author_detail.html', {'author': author})

def add_comment(request):
    # Aquí iría la lógica para procesar la solicitud de agregar un nuevo comentario
    return HttpResponse("Placeholder para agregar un nuevo comentario")

def create_or_update_post(request):
    # Aquí iría la lógica para procesar la solicitud de agregar un nuevo comentario
    return HttpResponse("Placeholder para agregar un nuevo comentario")
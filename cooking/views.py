from django.shortcuts import render, redirect
from .models import Category, Posts
from django.db.models import F
from .forms import PostAddForm


def index(request):
    posts = Posts.objects.all()
    context = {
        'title': 'Главная страница',
        'posts': posts,
    }

    return render(request, 'cooking/index.html', context)


def category_list(request, pk):
    posts = Posts.objects.filter(category_id=pk)
    context = {
        'title': posts[0].category,
        'posts': posts,
    }

    return render(request, 'cooking/index.html', context)


def post_detail(request, pk):
    article = Posts.objects.get(pk=pk)
    Posts.objects.filter(pk=pk).update(watched=F('watched') + 1) # количество просмотра +1
    extend_post = Posts.objects.all().exclude(pk=pk).order_by('-watched')[:5]

    context = {
        'title': article.title,
        'post': article,
        'extend_posts': extend_post,
    }

    return render(request, 'cooking/article_detail.html', context)


def post_add(request):
    if request.method == 'POST':
        form = PostAddForm(request.POST, request.FILES)
        if form.is_valid():
            post = Posts.objects.create(**form.cleaned_data)
            post.save()
            return redirect('post_detail', post.pk)
    else:
        form = PostAddForm(request.POST)

    context = {
        'form': form,
        'title':'Добавить статью'
    }
    return render(request, 'cooking/article_add_form.html', context)

from django.shortcuts import render
from .models import Category, Posts



def index(request):
    posts = Posts.objects.all()
    categories = Category.objects.all()
    context = {
        'title': 'Главная страница',
        'posts': posts,
        'categories': categories,
    }

    return render(request, 'cooking/index.html', context)


def category_list(request, pk):
    posts = Posts.objects.filter(category_id=pk)
    categories = Category.objects.all()
    context = {
        'title': posts[0].category,
        'posts': posts,
        'categories': categories,
    }

    return render(request, 'cooking/index.html', context)
from django.shortcuts import render
from .models import Category, Posts

def index(request):
    posts = Posts.objects.all()

    context = {
        'title': 'Главная страница',
        'posts': posts
    }

    return render(request, 'cooking/index.html', context)
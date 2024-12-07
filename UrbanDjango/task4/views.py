from lib2to3.fixes.fix_input import context

from django.shortcuts import render
from django.views.generic import TemplateView

#Create your views here.
def index_func(request):
    title = "Главная"
    text = "Главная страница"
    context = {
        'title': title,
        'text': text,
    }
    return render(request, 'index.html', context)

def shop_play(request):
    title = "Магазин"
    text = "Игры"
    games = [
        "Atomic Heart",
        "Cyberpunk 2077",
        "PayDay 2"
    ]
    context = {
        'title': title,
        'text': text,
        'games': games
    }
    return render(request, 'shop.html', context)

def basket(request):
    title = "Корзина"
    text = "Корзина"
    context = {
        'title': title,
        'text': text,
    }
    return render(request, 'basket.html', context)

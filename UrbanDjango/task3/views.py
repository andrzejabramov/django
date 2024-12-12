from lib2to3.fixes.fix_input import context
from django.shortcuts import render
from django.views.generic import TemplateView

#Create your views here.
def index_func(request):
    title = "Главная"
    text = "Главная страница"
    first = "Atomic Heart"
    second = "Cyberpunk 2077"
    third = "PayDay 2"
    context = {
        'title': title,
        'text': text,
        'first': first,
        'second': second,
        'third': third,
    }
    return render(request, 'index.html', context)

def shop_play(request):
    title = "Магазин"
    text = "Игры"
    first = "Atomic Heart"
    second = "Cyberpunk 2077"
    third = "PayDay 2"
    context = {
        'title': title,
        'text': text,
        'first': first,
        'second': second,
        'third': third,
    }
    return render(request, 'shop.html', context)

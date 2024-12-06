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

# Один вариант класса:
class index_class(TemplateView):
    template_name = 'shop.html'
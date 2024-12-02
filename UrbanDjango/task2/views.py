from django.shortcuts import render
from django.views.generic import TemplateView

#Create your views here.
def index_func(request):
    return render(request, 'index_func.html')

# Один вариант класса:
# class index_class(TemplateView):
#     template_name = 'index_class.html'


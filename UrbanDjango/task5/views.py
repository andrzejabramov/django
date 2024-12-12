from django.http import HttpResponse
from django.shortcuts import render
from .forms import UserRegister

# Create your views here.
def sign_up_by_html(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        print(f'username: {username}')
        print(f'password: {password}')
        print(f'repeat_password: {repeat_password}')
        print(f'age: {age}')

        return HttpResponse('Форма успешно отправлена')
    return render(request, 'registration_page.html')

def sign_up_by_django(request):
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
    else:
        form = UserRegister()
    return render(request, 'registration_page.html', {'form': form})

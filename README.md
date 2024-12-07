## Домашнее задание по Django проекту:

#### Исполнено Андреем Абрамовым

##  I. Начало
### 
1. Создаем pycharm проект
2. В виртуальное окружение устанавливаем Django:  
```pip install django```
3. Создаем проект Django с именем UrbanDjango:   
```django-admin startproject UrbanDjango``` 
4. Переходим в директорию django проекта:  
```cd UrbanDjango```
5. Запускаем сервер django:  
```python3 manage.py runserver```  
Результат:
![screen1](screens/runserver.png)  
6. Добавляем приложения в Django проект (UrbanDjango): согласно задания это приложения:
- example1
- example2
- example3
- task2  
Проверяем, что находимся в директории UrbanDjango  
```python3 manage.py startapp example1```  
```python3 manage.py startapp example2```  
```python3 manage.py startapp example3```  
```python3 manage.py startapp task2```  
7. Находим в рабочем приложении (по текущему заданию это task2) файл views.py
и настраиваем функциональное представление:  
![screen2](screens/function_view.png)  
8. Прописываем путь к шаблонам в файле settings.py Django проекта:  
![screen3](screens/Templates_path.png)  
9. В этом же файле настроекм в список установленных приложений добавляем наше рабочее:  
![screen4](screens/Installed_apps.png)  
10. Подготовим шаблон страницы для вывода текста с помощью функционального представления:  
![screen5](screens/template_func.png)  
11. В файле urls.py Django проекта свяжем url с шаблоном:  
![screen6](screens/path_func.png)  
12. Запускаем приложение и получаем нужный текст в броузере:  
![screen7](screens/res_func.png)  
13. Создаем первый вариант классового представления м помощью класса, наследующего TemplateView  
Файл views.py приложения:  
![screen8](screens/view_class.png)  
Файл urls.py django проекта:  
![screen9](screens/url_class.png)
Результат в броузере:
![screen10](screens/res_class.png)
14. Второй (упрощенный) вариант классового представления:  
Комментируем в файле приложения views.py созданный нами класс
![screen11](screens/view_class_comment.png)  
Вносим изменения в файл django проекта urls.py:  
![screen13](screens/url_class_light.png)
Получаем нужный результат в броузере:
![screen13](screens/res_class_light.png)
15. Использование переменных views в шаблоне:
```commandline
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>{{ title }}</title>
</head>
<body>
    <h1 align="center">{{ text }}</h1>
    <h2 align="center"><a href="#">Главная</a></h2>
    <h2 align="center"><a href="/shop">Магазин</a></h2>
    <h2 align="center"><a href="/basket">Корзина</a></h2>
</body>
</html>
```
Переменная {{ title }}  и {{ text }} подтягива.тся из файла views.py, где они определены переменной context:
```commandline
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
```




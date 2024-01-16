from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(request):
    return HttpResponse("Hello World")

def goodbye(request):
    return HttpResponse("Good Bye")

def index(request):
    context = {
        'page_name': "Главная страница",
        'title': "__ Главная страница ___",
        'description': "Описание",
        'jobs': ["Курьер", "Шеф-повар", "Строитель", "Админ"]
    }
    return render(request, "index.html", context)


def contact(request):
    context = {
        'page_name': "Контакты",
        'title': "Это страница контакты",
        'phone': "0771244745",
        'instagram': "Username"
    }
    return render(request, 'contact.html', context)

def test(request):
    context = {
        'page_name': "Тест",
        'title': "test"
    }
    return render(request, 'test.html', context)
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {
        'title': 'Home - Главная',
        'content': 'Магазин мебели HOME',
    }
    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'Home - О нас',
        'content': 'О нас',
        'text_on_page': 'Далеко-далеко за словесными горами в стране гласных и согласных, живут рыбные тексты. Одна предупреждал грустный оксмокс, на берегу языкового пор буквенных переписали составитель власти продолжил силуэт однажды рыбными первую, она переулка ему. Предупреждал.'
    }
    return render(request, 'main/about.html', context)
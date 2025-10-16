from django.shortcuts import render
from django.http import HttpResponse

from goods.models import Categories


def index(request):

    context = {
        'title': 'Главная PBC',
        'content': 'Подарок в большом',
        'content_1': 'городе'
    }
    return render(request, 'main/index.html', context)

def aboutas(request):
    text_on_page = 'Команда мастеров, декорирует изделия в разных стилях'

    context = {
        'title': 'PBC - О нас',
        'content': 'О нас',
        'text_on_page': text_on_page
    }
    return render(request, 'main/aboutas.html', context)






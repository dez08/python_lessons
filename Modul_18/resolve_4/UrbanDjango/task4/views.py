from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


def platform(request):
    return render(request, "fourth_task/platform.html")


def games(request):
    page_name = "Игры"
    games_list = ["Atomic Heart",
                            "Cyberpunk 2077",
                            "PayDay 2"]
    buy = "Купить"
    context = {
        'title': page_name,
        'games_list': games_list,
        'buy': buy,
    }
    return render(request, 'fourth_task/games.html', context)


def cart(request):
    page_name = "Корзина"
    img = "/photo/Корзина.jpg"
    text_1 = "Извините, ваша корзина пуста."
    context = {
        'title': page_name,
        'img': img,
        'text_1': text_1,
    }
    return render(request, 'fourth_task/cart.html', context)


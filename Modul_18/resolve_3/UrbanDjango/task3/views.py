from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


def platform(request):
    return render(request, "third_task/platform.html")


def games(request):
    page_name = "Игры"
    game_1 = "Atomic Heart"
    img_1 = "/static/Atomic_Heart_Art.jpg"
    game_2 = "Cyberpunk 2077"
    img_2 = "/static/Cyberpunk_2077.jpg"
    game_3 = "PayDay 2"
    img_3 = "/static/Payday2.jpg"
    buy = "Купить"
    context = {
        'title': page_name,
        'game_1': game_1,
        'img_1': img_1,
        'game_2': game_2,
        'img_2': img_2,
        'game_3': game_3,
        'img_3': img_3,
        'buy': buy,
    }
    return render(request, 'third_task/games.html', context)


def cart(request):
    page_name = "Корзина"
    img = "/static/Корзина.jpg"
    text_1 = "Извините, ваша корзина пуста."
    context = {
        'title': page_name,
        'img': img,
        'text_1': text_1,
    }
    return render(request, 'third_task/cart.html', context)


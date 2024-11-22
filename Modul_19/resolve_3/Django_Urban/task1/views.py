from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister
from .models import Buyer, Game
# Create your views here.


def platform(request):
    return render(request, "fourth_task/platform.html")


def games(request):
    page_name = "Игры"
    games_list = Game.objects.all()
    context = {
        'title': page_name,
        'games_list': games_list,
    }
    return render(request, 'fourth_task/games.html', context)


def cart(request):
    page_name = "Корзина"
    text_1 = "Извините, ваша корзина пуста."
    context = {
        'title': page_name,
        'text_1': text_1,
    }
    return render(request, 'fourth_task/cart.html', context)


def sign_up_by_django(request):
    if request.method == 'POST':
        form = UserRegister(request.POST)
        info = {}

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if Buyer.objects.filter(name=username).exists():
                info['error'] = 'Пользователь уже существует'
            elif password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif int(age) < 18:
                info['error'] = 'Вы должны быть старше 18'
            else:
                Buyer.objects.create(name=username, age=age, balance=0.0)
                return HttpResponse(f'Приветствуем, {username}!')

        context = {'info': info, 'form': form}
        return render(request, 'fifth_task/registration_page.html', context)
    else:
        form = UserRegister()

    return render(request, 'fifth_task/registration_page.html', {'form': form})


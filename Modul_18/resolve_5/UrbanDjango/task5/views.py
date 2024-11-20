from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister


# Create your views here.
def start_page(request):
    return render(request, 'start_page.html')


def sign_up_by_django(request):
    users = ['Gregory', 'Alex', 'Anna', 'Victor']

    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            info = {}
            context = {'info': info, 'form': form}
            if password == repeat_password and age > 18 and username not in users:
                return HttpResponse(f'Приветствуем, {username}!')
            elif password != repeat_password:
                info['error'] = 'Пароли не совпадают'
                return render(request, 'fifth_task/registration_page.html', context)
            elif int(age) < 18:
                info['error'] = 'Вы должны быть старше 18'
                return render(request, 'fifth_task/registration_page.html', context)
            elif username in users:
                info['error'] = 'Пользователь уже существует'
                return render(request, 'fifth_task/registration_page.html', context)
    else:
        form = UserRegister()
    return render(request, 'fifth_task/registration_page.html', {'form': form})


def sign_up_by_html(request):
    users = ['Gregory', 'Alex', 'Anna', 'Victor']
    info = {}
    context = {
        'info': info
    }
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        if password == repeat_password and int(age) > 18 and username not in users:
            return HttpResponse(f'Приветствуем, {username}!')
        elif password != repeat_password:
            info['error'] = 'Пароли не совпадают'
            return render(request, 'fifth_task/registration_page.html', context)
        elif int(age) < 18:
            info['error'] = 'Вы должны быть старше 18'
            return render(request, 'fifth_task/registration_page.html', context)
        elif username in users:
            info['error'] = 'Пользователь уже существует'
            return render(request, 'fifth_task/registration_page.html', context)

    else:
        return render(request, 'fifth_task/registration_page.html')

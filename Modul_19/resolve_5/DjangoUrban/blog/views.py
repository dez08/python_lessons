from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Post


# Create your views here.


def post_list(request):
    post_list = Post.objects.all()
    items_per_page = request.GET.get('items_per_page', 5)  # Устанавливаем 5 по умолчанию
    paginator = Paginator(post_list, items_per_page)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    return render(request, 'blog/post_list.html', {'posts': posts, 'items_per_page': items_per_page})

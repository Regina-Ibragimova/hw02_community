from django.shortcuts import HttpResponse

# Create your views here.

from django.shortcuts import render, get_object_or_404
from .models import Post,Group

# Главная страница
def index(request):    
    template = 'posts/index.html'

    posts = Post.objects.order_by('-pub_date')[:10]

    title = 'Последние обновления'
    context = {
        'title' : title,
        'posts' : posts
    }
    return render(request, template, context)


# Страница со списком групп
def group_posts(request,slug):
    

    group = get_object_or_404(Group, slug=slug)

    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]

    title = 'Записи сообщества '+str(group)
    #text = 'Здесь будет информация о группах проекта Yatube'
    context = {
        'group': group,
        'posts' : posts,
        'title' : title
    }
    return render(request, 'posts/group_list.html', context)




    


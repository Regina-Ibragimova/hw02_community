from django.shortcuts import get_object_or_404, render

from .models import Group, Post


def index(request):
    template = 'posts/index.html'

    posts = Post.objects.order_by('-pub_date')[:10]

    title = 'Последние обновления'
    context = {
        'title': title,
        'posts': posts
    }
    return render(request, template, context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group)[:10]
    title = f'Записи сообщества {group}'
    context = {
        'group': group,
        'posts': posts,
        'title': title
    }
    return render(request, 'posts/group_list.html', context)

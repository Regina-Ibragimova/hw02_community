# posts/urls.py
from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
#главная страница
    path('', views.index, name='index'),
#страница группы 
    path('group/<slug:slug>/', views.group_posts, name = 'group_list'),   
    
] 
from django.contrib import admin
from django.urls import path

from posts import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cats', views.allcats, name='cats'),
    path('<int:post_id>/post', views.getpost, name='getpost'),
    path('<int:cat_id>/category', views.viewCat, name='viewcat')
]
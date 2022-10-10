from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Category


def index(request):
    posts = Post.objects.all()
    context = {"posts": posts}
    return render(request, 'posts.html', context)


def getpost(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {"post": post}
    return render(request, 'post.html', context)

def allcats(request):
    cats = Category.objects.all()
    context = {"cats": cats}
    return render(request, 'cats.html', context)


def viewCat(request, cat_id):
    cat = Category.objects.get(id=cat_id)
    context = {"cat": cat}
    return render(request, 'cat.html', context)

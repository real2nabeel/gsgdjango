from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField(max_length=100)

class Category(models.Model):
    catName = models.CharField(max_length=20)
    catDesc = models.TextField(max_length=100)

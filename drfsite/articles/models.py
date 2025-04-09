from django.contrib.auth.models import User
from django.db import models


class Article(models.Model):
    name = models.CharField(max_length=250, unique=True)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)
    author = models.ForeignKey(User, verbose_name='author', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name

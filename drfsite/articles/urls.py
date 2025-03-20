from django.urls import path
from drfsite.articles import views

urlpatterns = [
    path('', views.index),
]

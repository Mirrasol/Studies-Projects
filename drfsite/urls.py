"""
URL configuration for drfsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from rest_framework import routers

from drfsite import views
from drfsite.articles.views import *


urlpatterns = [
    path('api/v1/articles/', ArticlesAPIList.as_view()),
    path('api/v1/articles/<int:pk>/', ArticlesAPIUpdate.as_view()),
    path('api/v1/articlesdelete/<int:pk>/', ArticlesAPIDestroy.as_view()),
    path('admin/', admin.site.urls),
]

# ---------------------------------------------------------------------------------------
# Lesson 9.
# Custom router.
# class MyCustomRouter(routers.SimpleRouter):
#     routes = [
#         routers.Route(url=r'^{prefix}$/',
#                       mapping={'get': 'list'},
#                       name='{basename}-list',
#                       detail=False,
#                       initkwargs={'suffix': 'List'}),
#         routers.Route(url=r'^{prefix}/{lookup}$/',
#                       mapping={'get': 'retrieve'},
#                       name='{basename}-detail',
#                       detail=True,
#                       initkwargs={'suffix': 'Detail'}),
#     ]
#
# router = MyCustomRouter()
#
# router = routers.DefaultRouter()
# router.register(r'articles', ArticlesViewSet, basename='articles')  
# # basename задаст имя параметров (articles-list, articles-detail etc) вместо имени модели (article) 
# # => обязателен там, где нет qyeryset и не подставить модель автоматом
# print(router.urls)
#
# urlpatterns = [
#     path('', views.index),
#     path('api/v1/', include(router.urls)),
#     path('admin/', admin.site.urls),
# ]
#
# ---------------------------------------------------------------------------------------
# Lesson 8-1.
# Без роутеров.
# urlpatterns = [
#     path('', views.index),
#     path('api/v1/articleslist/', ArticlesViewSet.as_view({'get': 'list'})),
#     path('api/v1/articleslist/<int:pk>/', ArticlesViewSet.as_view({'put': 'update'})),
#     path('admin/', admin.site.urls),
# ]
#----------------------------------------------------------------------------------------
# Lesson 7.
# urlpatterns = [
#     path('', views.index),
#     path('api/v1/articleslist/', ArticlesAPIList.as_view()),
#     path('api/v1/articleslist/<int:pk>/', ArticlesAPIUpdate.as_view()),
#     path('api/v1/articlesdetail/<int:pk>/', ArticlesAPIDetailView.as_view()),
#     path('admin/', admin.site.urls),
# ]
#
from rest_framework import generics

from .models import Article
from .serializers import ArticlesSerializer


class ArticlesAPIView(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticlesSerializer

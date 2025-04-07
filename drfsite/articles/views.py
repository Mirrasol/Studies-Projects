# from django.forms import model_to_dict
# from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Article
from .serializers import ArticlesSerializer


# Lesson 4.
class ArticlesAPIView(APIView):
    def get(self, request):
        lst = Article.objects.all()
        return Response({'posts': ArticlesSerializer(lst, many=True).data})  # список записей, поэтому many
    
    def post(self, request):
        serializer = ArticlesSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        post_new = Article.objects.create(
            name=request.data['name'],
            body=request.data['body'],
            category_id=request.data['category_id'],
        )
        return Response({'post': ArticlesSerializer(post_new).data})

# Lesson 3.
# Учим базовый класс вьюх - APIView: без сериализаторов.
# class ArticlesAPIView(APIView):
#     def get(self, request):
#         lst = Article.objects.all().values()
#         return Response({'posts': list(lst)})
    
#     def post(self, request):
#         post_new = Article.objects.create(
#             name=request.data['name'],
#             body=request.data['body'],
#             category_id=request.data['category_id'],
#         )
#         return Response({'post': model_to_dict(post_new)})
#
# ------------------------------------------------------------------------
# Lesson 2.
# Смотрим пример того, как можно быстро писать вьюхи.
# class ArticlesAPIView(generics.ListAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticlesSerializer

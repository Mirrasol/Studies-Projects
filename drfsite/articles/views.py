# from django.forms import model_to_dict
# from rest_framework import generics
from rest_framework import mixins, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
# from rest_framework.views import APIView

from .models import Article, Category
from .serializers import ArticlesSerializer


# Lesson 9.
# Routers.
class ArticlesViewSet(mixins.CreateModelMixin,
                            mixins.RetrieveModelMixin,
                            mixins.UpdateModelMixin,
                            mixins.ListModelMixin,
                            viewsets.GenericViewSet):
#   queryset = Article.objects.all()
    serializer_class = ArticlesSerializer

    def get_queryset(self):  # когда надо переопределять для сложных запросов в бд, убирая queryset
        pk = self.kwargs.get("pk")
        if not pk:
            return Article.objects.all()[:3]
        return Article.objects.filter(pk=pk)

    @action(methods=['get'], detail=True)
    def category(self, request, pk=None):
        categories = Category.objects.get(pk=pk)
        return Response({'categories': categories.name})

# декоратор на список записей:
#     @action(methods=['get'], detail=False)  # True = одна запись, False = список записей
#     def category(self, request):  # имя метода задает имя маршрута
#         categories = Category.objects.all()
#         return Response({'categories': [c.name for c in categories]})
#
# ---------------------------------------------------------------------------------------
# Lesson 8.
# Viewsets, ModelViewSets.
# class ArticlesViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = Article.objects.all()
#     serializer_class = ArticlesSerializer
#
# аналог с миксинами.
# class ArticlesMixinsViewSet(mixins.CreateModelMixin,
#                             mixins.RetrieveModelMixin,
#                             mixins.UpdateModelMixin,
#                             mixins.ListModelMixin,
#                             viewsets.GenericViewSet):
#     queryset = Article.objects.all()
#     serializer_class = ArticlesSerializer
#
# ---------------------------------------------------------------------------------------
# Lesson 7.
# UpdateAPIView, RetrieveUpdateDestroyAPIView.
# class ArticlesAPIUpdate(generics.UpdateAPIView):
#     queryset = Article.objects.all()  # ленивый запрос => выберутся не все записи, а только нужные
#     serializer_class = ArticlesSerializer
#
#
# class ArticlesAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticlesSerializer
#
# # -------------------------------------------------------------------------------------
# # Lesson 6.
# # ModelSerializer, ListCreateAPIView = методы GET + POST.
# class ArticlesAPIList(generics.ListCreateAPIView):
#     queryset = Article.objects.all()  # ссылается на список записей, кот. возвращаем клиенту
#     serializer_class = ArticlesSerializer
#
#
# # -------------------------------------------------------------------------------------
# Lesson 5.
# Methods save/update/create.
# class ArticlesAPIView(APIView):
#     def get(self, request):
#         lst = Article.objects.all()
#         return Response({'posts': ArticlesSerializer(lst, many=True).data})  # список записей, поэтому many
#
#     def post(self, request):
#         serializer = ArticlesSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         return Response({'post': serializer.data})
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method PUT not allowed"})
#
#         try:
#             instance = Article.objects.get(pk=pk)
#         except:
#             return Response({"error": "Object not found"})
#
#         serializer = ArticlesSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"post": serializer.data})
#
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method DELETE not allowed"})
#
#         try:
#             instance = Article.objects.get(pk=pk)
#             instance.delete()
#         except:
#             return Response({"error": "Object not found"})
#
#         return Response({"post": "delete post " + str(pk)})
#
# # -------------------------------------------------------------------------------------
# Lesson 4.
# class ArticlesAPIView(APIView):
#     def get(self, request):
#         lst = Article.objects.all()
#         return Response({'posts': ArticlesSerializer(lst, many=True).data})  # список записей, поэтому many
#
#     def post(self, request):
#         serializer = ArticlesSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#
#         post_new = Article.objects.create(
#             name=request.data['name'],
#             body=request.data['body'],
#             category_id=request.data['category_id'],
#         )
#         return Response({'post': ArticlesSerializer(post_new).data})
#
# ---------------------------------------------------------------------------------------
# Lesson 3.
# Учим базовый класс вьюх - APIView: без сериализаторов.
# class ArticlesAPIView(APIView):
#     def get(self, request):
#         lst = Article.objects.all().values()
#         return Response({'posts': list(lst)})
#
#     def post(self, request):
#         post_new = Article.objects.create(
#             name=request.data['name'],
#             body=request.data['body'],
#             category_id=request.data['category_id'],
#         )
#         return Response({'post': model_to_dict(post_new)})
#
# ---------------------------------------------------------------------------------------
# Lesson 2.
# Смотрим пример того, как можно быстро писать вьюхи.
# class ArticlesAPIView(generics.ListAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticlesSerializer
#
# import io

from rest_framework import serializers

# from rest_framework.parsers import JSONParser
# from rest_framework.renderers import JSONRenderer
from .models import Article


# Lesson 10.
# Permissions.
class ArticlesSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())  # связываем автора с текущим юзером и скрываем это поле
    class Meta:
        model = Article
        fields = ["name", "body", "author", "category"]  # можно в кортеже, можно "__all__"

# Lesson 6.
# ModelSerializer, ListCreateAPIView.
# class ArticlesSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Article
#         fields = ["name", "body", "author", "category"]  # можно в кортеже, можно "__all__"
#
# --------------------------------------------------------------------------------------
# Lesson 5.
# Methods save/update/create.
# class ArticlesSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=250)
#     body = serializers.CharField()
#     created_at = serializers.DateTimeField(read_only=True)
#     updated_at = serializers.DateTimeField(read_only=True)
#     category_id = serializers.IntegerField()
#
#     def create(self, validated_data):  # если указать просто data - будет метод create
#         return Article.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):  # если указать и data, и instance - определит метод update
#         instance.name = validated_data.get("name", instance.name)
#         instance.body = validated_data.get("body", instance.body)
#         instance.updated_at = validated_data.get("updated_at", instance.updated_at)
#         instance.category_id = validated_data.get("category_id", instance.category_id)
#         instance.save()
#         return instance
#
# --------------------------------------------------------------------
# Lesson 4-2.
# # Practice.
# class ArticlesSerializer(serializers.Serializer):
#     """From .models - Article."""
#     name = serializers.CharField(max_length=250)
#     body = serializers.CharField()
#     created_at = serializers.DateTimeField(read_only=True)
#     updated_at = serializers.DateTimeField(read_only=True)
#     category_id = serializers.IntegerField()
#
# ---------------------------------------------------------------------
# Lesson 4-1.
# Theory.
# class ArticlesModel:
#     def __init__(self, name, body):
#         self.name = name
#         self.body = body
#
#
# class ArticlesSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=255)  # должно совпасть с self
#     body = serializers.CharField()  # должно совпасть с названием в self
#
#
# def encode():
#     """ Кодируем преобразование объектов ArticlesModel
#     в JSON-format."""
#     model = ArticlesModel('Aloy', 'Content: Aloy Ahoy!')
#     model_sr = ArticlesSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep='\n')
#     json = JSONRenderer().render(model_sr.data)
#     print(json)
#
#
# def decode():
#     stream = io.BytesIO(b'{"name":"Aloy","body":"Content: Aloy Ahoy!"}')  # имитируем клиента
#     data  = JSONParser().parse(stream)
#     serializer = ArticlesSerializer(data=data)  # декодируем данные
#     serializer.is_valid()
#     print(serializer.validated_data)  # вернет объект-словарь
#
# ----------------------------------------------------------------------------
# Lesson 2.
# A serializer example.
# class ArticlesSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Article
#         fields = ('name', 'body', 'category')
#
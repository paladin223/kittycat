import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

# from cats.models import Cat


class InfoModel:
    def __init__(self, name, content):
        self.name = name
        self.content = content


class InfoSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    content = serializers.CharField()


# создаем экземпляр модели -> сериализуем -> json'им
# поля модели === поля сериалайзера
def encode():
    model = InfoModel("user", "info about user")
    serialized = InfoSerializer(model)
    print(serialized)
    print(serialized.data)
    json = JSONRenderer().render(serialized.data)
    print(json)


# парсим json -> сериализуем -> данные
# поля json'а === поля сериалайзера
def decode():
    stream = io.BytesIO(b'{"name":"user","content":"info about user"}')
    data = JSONParser().parse(stream)
    serializers = InfoSerializer(data=data)
    serializers.is_valid()
    print(serializers.validated_data)


class HomepageSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    slug = serializers.SlugField(max_length=255)
    age = serializers.IntegerField()
    weight = serializers.IntegerField()
    photo = serializers.ImageField()
    color_id = serializers.IntegerField()
    is_published = serializers.BooleanField(default=True)

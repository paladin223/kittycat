from rest_framework import serializers

from cats.models import Cat


class HomepageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cat
        fields = ("name", "slug")

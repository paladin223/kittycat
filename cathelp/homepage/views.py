from django.views.generic import ListView
from rest_framework.response import Response

# from rest_framework import generics
from rest_framework.views import APIView

from cats.models import Cat
from homepage.serializers import HomepageSerializer


class HomepageAPIView(APIView):
    # queryset = Cat.objects.all()
    # serializer_class = HomepageSerializer
    def get(self, request):
        cats = Cat.objects.all().values()
        return Response({"get": HomepageSerializer(cats, many=True).data})

    def post(self, request):
        serializer = HomepageSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        new_cat = Cat.objects.create(
            name=request.data["name"],
            slug=request.data["slug"],
            age=request.data["age"],
            weight=request.data["weight"],
            photo=request.data["photo"],
            color_id=request.data["color_id"],
            is_published=request.data["is_published"],
        )
        return Response({"post": HomepageSerializer(new_cat).data})


class Homepage(ListView):
    template_name = "homepage/homepage.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        # context = super().get_context_data(**kwargs)
        # context["name"] = name
        # return context
        return super().get_context_data(**kwargs)

    def get_queryset(self):
        pass

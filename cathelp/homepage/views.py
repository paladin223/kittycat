from django.views.generic import ListView
from rest_framework import generics

from cats.models import Cat
from homepage.serializers import HomepageSerializer


class HomepageAPIView(generics.ListAPIView):
    queryset = Cat.objects.all()
    serializer_class = HomepageSerializer


class Homepage(ListView):
    template_name = "homepage/homepage.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        # context = super().get_context_data(**kwargs)
        # context["name"] = name
        # return context
        return super().get_context_data(**kwargs)

    def get_queryset(self):
        pass

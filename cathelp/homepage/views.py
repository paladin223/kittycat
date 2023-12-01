from django.forms import model_to_dict
from django.views.generic import ListView
# from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from cats.models import Cat
from users.models import User

# from homepage.serializers import HomepageSerializer


class HomepageAPIView(APIView):
    # queryset = Cat.objects.all()
    # serializer_class = HomepageSerializer
    def get(self, request):
        lst = Cat.objects.all().values()
        return Response({"cats": list(lst)})

    def post(self, request):
        new_user = User.objects.create(
            name=request.data["name"],
            email=request.data["email"],
            password=request.data["password"],
        )
        return Response({"user": model_to_dict(new_user)})


class Homepage(ListView):
    template_name = "homepage/homepage.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        # context = super().get_context_data(**kwargs)
        # context["name"] = name
        # return context
        return super().get_context_data(**kwargs)

    def get_queryset(self):
        pass

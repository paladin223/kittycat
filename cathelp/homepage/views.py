from django.shortcuts import render

from cats.models import Cat


def homepage(request):
    cats = Cat.objects.all()
    context = {"cats": cats}
    return render(request, "homepage.html", context)

from django.shortcuts import render
from django.http import HttpResponse

from cats.models import Cat


def list_items(request):
    print(request.GET)
    cats = Cat.objects.all()
    context = {"cats": cats,
               "uri": "cats/list.html"}
    return render(request, "cats/cats.html", context)


def one_cat(request, catid: int) -> HttpResponse:
    cats = Cat.objects.all()
    if 0 <= catid <= len(cats):
        cats = Cat.objects.all()
        context = {"cats": [cats[catid]],
                   "uri": "cats/list.html"}
        return render(request, "cats/cats.html", context)
    else:
        return HttpResponse("Ошибка :(")
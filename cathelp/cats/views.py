# from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from cats.models import Cat


def list_items(request):
    print(request.GET)
    print(request.session)
    context = {}
    return render(request, "cats/cats.html", context)


def one_cat(request, catslug) -> HttpResponse:
    cat = get_object_or_404(Cat, slug=catslug)
    context = {"cat": cat}
    return render(request, "cats/info.html", context)

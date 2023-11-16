# from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.shortcuts import render
import cats.forms
import cats.models


def list_items(request):
    print(request.GET)
    print(request.session)
    context = {}
    return render(request, "cats/cats.html", context)


def one_cat(request, catslug) -> HttpResponse:
    cat = get_object_or_404(cats.models.Cat, slug=catslug)
    context = {"cat": cat}
    return render(request, "cats/info.html", context)


def add_cat(request):
    if request.method == "POST":
        form = cats.forms.AddCat(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            try:
                cats.models.Cat.objects.create(**form.cleaned_data)
                return redirect("homepage:home")
            except:
                form.add_error(None, "Ошибка добавления поста")
    else:
        form = cats.forms.AddCat(request.POST)
    context = {"form": form}
    return render(request, "cats/add_cat.html", context)

# from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import ListView

import cats.forms
import cats.models


class CatsList(ListView):
    model = cats.models.Cat
    template_name = "cats/list.html"
    context_object_name = "cats"

    # dynamic context
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["color_selected"] = ""
        context["colors"] = cats.models.Color.objects.all()
        return context

    def get_queryset(self):
        return cats.models.Cat.objects.filter(
            is_published=True,
        ).exclude(photo__exact="")


class CatColor(ListView):
    model = cats.models.Cat
    template_name = "cats/list.html"
    context_object_name = "cats"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["color_selected"] = self.kwargs["color_slug"]
        context["colors"] = cats.models.Color.objects.all()
        return context

    def get_queryset(self):
        return cats.models.Cat.objects.filter(
            color__slug=self.kwargs["color_slug"],
            is_published=True,
        ).exclude(photo__exact="")


class CatDetail(DetailView):
    model = cats.models.Cat
    template_name = "cats/info.html"
    slug_url_kwarg = "cat_slug"
    context_object_name = "cat"

    def get_context_data(self, *, object_list=None, **kwargs):
        # context = super().get_context_data(**kwargs)
        # context["name"] = name
        # return context
        return super().get_context_data(**kwargs)


class CatCreate(CreateView):
    form_class = cats.forms.AddCat
    template_name = "cats/add.html"
    success_url = reverse_lazy("homepage:home")

    def form_valid(self, form):
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)

from django.contrib.auth.decorators import login_required
from django.db.models import Exists
from django.db.models import OuterRef
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import ListView

import cats.forms
import cats.models
import cats.utils
from users.models import User


class CatsList(cats.utils.ListCatMixin, ListView):
    model = cats.models.Cat
    template_name = "cats/list.html"
    context_object_name = "cats"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        extras = self.get_user_data()
        return dict(list(context.items()) + list(extras.items()))

    def get_queryset(self):
        queryselect = cats.models.Cat.objects
        if self.request.user.is_authenticated:
            queryselect = queryselect.annotate(
                liked=Exists(
                    User.objects.filter(
                        like=OuterRef("id"), id=self.request.user.id
                    )
                )
            )
        return (
            queryselect.filter(
                is_published=True,
            )
            .exclude(photo__exact="")
            .select_related("color")
        )


class CatColor(cats.utils.ListCatMixin, ListView):
    model = cats.models.Cat
    template_name = "cats/list.html"
    context_object_name = "cats"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        extras = self.get_user_data()
        context["color_selected"] = self.kwargs["color_slug"]
        return dict(list(context.items()) + list(extras.items()))

    def get_queryset(self):
        if self.request.user.is_authenticated:
            queryselect = cats.models.Cat.objects.annotate(
                liked=Exists(
                    User.objects.filter(
                        like=OuterRef("id"), id=self.request.user.id
                    )
                )
            )
        return (
            queryselect.filter(
                color__slug=self.kwargs["color_slug"],
                is_published=True,
            )
            .exclude(photo__exact="")
            .select_related("color")
        )


class CatDetail(DetailView):
    model = cats.models.Cat
    template_name = "cats/info.html"
    slug_url_kwarg = "cat_slug"
    context_object_name = "cat"

    def get_context_data(self, *, object_list=None, **kwargs):
        return super().get_context_data(**kwargs)


@method_decorator(login_required, name="dispatch")
class CatCreate(CreateView):
    form_class = cats.forms.AddCat
    template_name = "cats/add.html"
    success_url = reverse_lazy("homepage:home")

    def form_valid(self, form):
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)


class LikeCatView(View):
    def post(self, request, cat_slug):
        cat = get_object_or_404(cats.models.Cat, slug=cat_slug)
        user = request.user

        # Проверяем, аутентифицирован ли пользователь
        if not user.is_authenticated:
            return JsonResponse({"auth": "false"})

        # Проверяем, не лайкнул ли уже текущий пользователь этого кота
        if user in cat.like.all():
            cat.like.remove(user)
            return JsonResponse(
                {
                    "auth": "true",
                    "message": "Лайк успешно удален",
                }
            )

        # Если пользователь еще не поставил лайк, добавляем его
        cat.like.add(request.user)
        return JsonResponse(
            {"auth": "true", "message": "Лайк успешно добавлен"}
        )

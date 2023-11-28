from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse
from django.urls import reverse_lazy
from django.views import View

import users.forms


class Login(LoginView):
    form_class = users.forms.Authentication
    template_name = "users/login.html"
    success_url = reverse_lazy("homepage:home")

    def form_valid(self, form):
        email = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        user = authenticate(username=email, password=password)
        if user is not None:
            login(self.request, user)

        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)


class Logout(LogoutView):
    def get(self, request, *args, **kwargs):
        logout(request)
        next_url = request.GET.get("next", None)
        if next_url:
            return redirect(next_url)
        return redirect(reverse("homepage:home"))


class Registration(View):
    template_name = "users/register.html"  # Замените на ваш шаблон регистрации
    form_class = users.forms.Register

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("homepage:home")
        return render(request, self.template_name, {"form": form})

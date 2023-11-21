from django.urls import path

import users.views

app_name = "users"

urlpatterns = [
    path("login/", users.views.Login.as_view(), name="login"),
    path("logout/", users.views.Logout.as_view(), name="logout"),
    path("register/", users.views.Registration.as_view(), name="register"),
]

from django.urls import path

from . import views

app_name = "homepage"

urlpatterns = [
    path("", views.Homepage.as_view(), name="home"),
    path("api", views.HomepageAPIView.as_view(), name="home_api"),
]

from django.urls import path

from . import views

app_name = "cats"

urlpatterns = [
    path("", views.CatsList.as_view(), name="cats_list"),
    path("<slug:cat_slug>/", views.CatDetail.as_view(), name="one_cat"),
    path("color/<slug:color_slug>/", views.CatColor.as_view(), name="color"),
    path("add", views.CatCreate.as_view(), name="add"),
]

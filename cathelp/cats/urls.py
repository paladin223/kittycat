from django.urls import path

from . import views

app_name = "cats"

urlpatterns = [
    path("", views.CatsList.as_view(), name="cats_list"),
    path("<slug:catslug>/", views.CatDetail.as_view(), name="one_cat"),
    path("add", views.CatCreate.as_view(), name="add"),
]

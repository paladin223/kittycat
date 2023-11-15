from django.urls import path

from . import views

app_name = "cats"

urlpatterns = [
    path("", views.list_items, name="cats_list"),
    path("<slug:catslug>/", views.one_cat, name="one_cat"),
    path("add", views.add_cat, name="add")
]

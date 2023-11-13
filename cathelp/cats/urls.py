from django.urls import path

from . import views

app_name = "cats"

urlpatterns = [
    path("", views.list_items, name="cats_list"),
    path("<int:catid>/", views.one_cat, name="one_cat")
]

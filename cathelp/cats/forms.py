from django import forms
import cats.models


class AddCat(forms.Form):
    name = forms.CharField(
        max_length=255, label="Кличка",
        widget=forms.TextInput(attrs={"class": "add-cat-input"}))
    slug = forms.SlugField(
        max_length=255,
        required="False",
        label="Eng кличка",
        widget=forms.TextInput(attrs={"class": "add-cat-input"}))
    age = forms.IntegerField(
        label="Возраст",
        widget=forms.TextInput(attrs={"class": "add-cat-input"}))
    weight = forms.FloatField(
        label="Вес",
        widget=forms.TextInput(attrs={"class": "add-cat-input"}))
    color = forms.ModelChoiceField(
        queryset=cats.models.Color.objects.all(), label="цвет",
        empty_label="Категория не выбрана",
        widget=forms.Select(attrs={"class": "add-cat-input"})
    )

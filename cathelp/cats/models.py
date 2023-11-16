from django.db import models
import django.urls
import sorl.thumbnail


class Color(models.Model):
    name = models.CharField(max_length=100, verbose_name="Цвет")
    slug = models.SlugField(
        max_length=255, unique=True, db_index=True, verbose_name="URL"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "цвет"
        verbose_name_plural = "цвета"
        default_related_name = "colors"


class Cat(models.Model):
    def upload_to_folder(instance, filename):
        return f"photos/{instance.slug}/{instance.slug}.png"

    name = models.CharField(max_length=100, verbose_name="Имя кота")
    slug = models.SlugField(
        max_length=255, unique=True, db_index=True, verbose_name="URL"
    )
    age = models.IntegerField(verbose_name="Возраст кота")
    weight = models.FloatField(verbose_name="Вес кота")
    color = models.ForeignKey(
        Color, on_delete=models.SET_NULL, default=None, null=True
    )
    photo = models.ImageField(
        upload_to=upload_to_folder,
        null=True,
        blank=True,
        verbose_name="Фото"
    )

    @property
    def photo_detail(self):
        if self.photo:
            return sorl.thumbnail.get_thumbnail(
                self.photo, "800x800", crop="center"
            )

    @property
    def photo_info(self):
        if self.photo:
            return sorl.thumbnail.get_thumbnail(
                self.photo, "800x800", crop="center"
            )

    def get_absolute_url(self):
        return django.urls.reverse(
            "cats:one_cat", kwargs={"catslug": self.slug}
        )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "кот"
        verbose_name_plural = "коты"
        default_related_name = "cats"

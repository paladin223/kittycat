from django.db import models
import sorl.thumbnail


class Cat(models.Model):
    def upload_to_folder(instance, filename):
        return f"photos/{instance.name}/{instance.name}.png"

    @property
    def photo_detail(self):
        return sorl.thumbnail.get_thumbnail(
            self.photo, "150x150", crop="center"
        )

    name = models.CharField(max_length=100, verbose_name="Имя кота")
    age = models.IntegerField(verbose_name="Возраст кота")
    weight = models.FloatField(verbose_name="Вес кота")
    photo = models.ImageField(upload_to=upload_to_folder, null=True,
                              blank=True)

    class Meta:
        verbose_name = "кот"
        verbose_name_plural = "коты"
        default_related_name = "cats"

    def __str__(self):
        return self.name

from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Cat


class CatAdmin(admin.ModelAdmin):
    def photo_admin(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=100>")
        return None

    photo_admin.short_description = "Фоткарточка"

    list_display = ("name", "age", "weight", "photo_admin")


admin.site.register(Cat, CatAdmin)

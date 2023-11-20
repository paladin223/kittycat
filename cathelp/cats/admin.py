from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Cat
from .models import Color


class CatAdmin(admin.ModelAdmin):
    def photo_admin(self, obj):
        if obj.photo:
            return mark_safe(
                f"<img src='{obj.photo.url}'" f"width=100 height=100>"
            )
        return None

    photo_admin.short_description = "Фоткарточка"

    readonly_fields = ("photo_admin",)
    list_display = (
        "name",
        "slug",
        "age",
        "weight",
        "photo_admin",
        "is_published",
    )
    list_editable = ("is_published",)
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Cat, CatAdmin)


class ColorAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Color, ColorAdmin)

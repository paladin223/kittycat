from django import template

register = template.Library()


# Could not work, if not(INSTALLED_APPS в файле settings.py)
@register.inclusion_tag("cats/short.html")
def show_cat(cat, *args, **kwargs):
    return {"cat": cat}

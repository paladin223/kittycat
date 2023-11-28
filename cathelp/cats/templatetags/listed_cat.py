from django import template

register = template.Library()


# Could not work, if not(INSTALLED_APPS в файле settings.py)
@register.inclusion_tag("cats/short.html")
def show_cat(cat, user, *args, **kwargs):
    context = {"cat": cat}
    if user.is_authenticated:
        context["user"] = user
    else:
        context["user"] = None
    return context

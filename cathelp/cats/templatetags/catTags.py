from django import template

from cats.models import Cat

register = template.Library()


# Could not work, if not(INSTALLED_APPS в файле settings.py)
@register.inclusion_tag("cats/list.html")
def show_cats(selector=None):
    cats = Cat.objects.all()
    return {"cats": cats}

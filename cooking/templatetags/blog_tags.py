from django import template
from cooking.models import Category

register = template.Library()

@register.simple_tag()
def get_category_names():
    return Category.objects.all()

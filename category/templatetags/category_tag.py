from django import template
from category.models import Category

register = template.Library()

@register.simple_tag
def get_category():
    all_category = Category.objects.all()
    return all_category
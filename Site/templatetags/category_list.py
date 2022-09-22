from django import template

from Site.models import Category

register = template.Library()


@register.inclusion_tag('news/tpl/list_categories_tpl.html')
def list_categories():
    categories = set(Category.objects.filter(posts__isnull=False))
    return {'categories': categories}

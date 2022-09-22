from django import template

from Site.models import Category

register = template.Library()


@register.inclusion_tag('news/tpl/menu_tpl.html')
def show_menu(menu_class='menu'):
    categories = Category.objects.all()
    return {'categories': categories, 'menu_class': menu_class}

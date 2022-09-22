from django import template

from Site.models import Tag

register = template.Library()


@register.inclusion_tag('news/tpl/list_tags_tpl.html')
def tags_widget():
    tags = set(Tag.objects.filter(posts__isnull=False))
    return {'tags': tags}

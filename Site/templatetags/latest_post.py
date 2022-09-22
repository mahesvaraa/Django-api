from django import template

from Site.models import Post

register = template.Library()


@register.inclusion_tag('news/tpl/latest_posts_tpl.html')
def latest_post():
    posts = Post.objects.all()[:4]
    return {'posts': posts}

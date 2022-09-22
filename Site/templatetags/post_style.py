from django import template

register = template.Library()


@register.inclusion_tag('news/tpl/post_tpl.html')
def show_post(post, div_class_0='', div_class_1='', div_class_2='', div_class_3=''):
    return {
        'post': post,
        'div_class_0': div_class_0,
        'div_class_1': div_class_1,
        'div_class_2': div_class_2,
        'div_class_3': div_class_3
    }

from django import template

register = template.Library()


@register.filter(name='range')
def html_range(start, stop, step=1):
    return [i for i in range(start, stop, step)]


@register.filter(name='get')
def dict_get(array, key):
    return array[key]
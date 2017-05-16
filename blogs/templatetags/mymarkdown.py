import markdown

from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter(is_safe=True)
@stringfilter
def mymarkdown(value):
    return mark_safe(markdown.markdown(value, ['extra']))
    
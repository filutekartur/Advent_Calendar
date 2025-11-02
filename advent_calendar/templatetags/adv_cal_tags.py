from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
@stringfilter    
def slice_to_dot_lr(value,arg):
    if isinstance(value,str):
        sliced=value.partition('.')
        if arg =='l':
            return sliced[0]
        if arg =='r':
            return sliced[2]


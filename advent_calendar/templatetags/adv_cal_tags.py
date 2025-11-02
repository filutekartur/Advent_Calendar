from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


def slice_to_sign(value,arg):
    if isinstance(str,value):
        l=value.split(arg)
        return l
    
@register.filter
@stringfilter    
def slice_to_dot_lr(value,arg):
    if isinstance(value,str):
        sliced=value.partition('.')
        if arg =='l':
            return sliced[0]
        if arg =='r':
            return sliced[2]


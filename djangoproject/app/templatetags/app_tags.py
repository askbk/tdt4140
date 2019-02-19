from django import template

register = template.Library()

@register.filter
def to_class_name(value):
    return value.__class__.__name__

@register.filter
def a_to_a(value):
    return value.replace("å","a")

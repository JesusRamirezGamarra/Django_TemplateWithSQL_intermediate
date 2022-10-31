from django import template
import random

register = template.Library()

@register.simple_tag
def get_random_int(a=1, b=2):
    if b is None:
        a, b = 0, a
    return random.randint(a, b)
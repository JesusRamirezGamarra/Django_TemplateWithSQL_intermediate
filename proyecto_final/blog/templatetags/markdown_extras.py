from django import template
from django.template.defaultfilters import stringfilter
from blog.models import Category,UserColaborator
import markdown as md

register = template.Library()


@register.filter()
@stringfilter
def markdown(value):
    return md.markdown(value, extensions=["markdown.extensions.fenced_code"])


@register.simple_tag
def get_categories():
    return Category.objects.all()[0:4]

@register.simple_tag
def get_colaboradores():
    # print(UserColaborator.objects.all()[0:4])
    return UserColaborator.objects.all()[0:4]


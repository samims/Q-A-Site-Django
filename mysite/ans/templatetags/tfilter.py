from django import template
register = template.Library()


@register.simple_tag
def get_item(ans):
    return dictionary.get()

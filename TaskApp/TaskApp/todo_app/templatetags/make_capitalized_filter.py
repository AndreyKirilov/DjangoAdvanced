from django import template

register = template.Library()


@register.filter(name='capitalize_chars')
def make_capitalized(text):
    if isinstance(text, str):
        return text.upper()

    return text

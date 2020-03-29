from django import template
register = template.Library()


@register.filter(name='add_class')
def add_attr(field, css_class):
    attrs = {
        "class": css_class
    }

    return field.as_widget(attrs=attrs)

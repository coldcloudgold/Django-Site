from django import template

register = template.Library()


@register.filter
def addclass(field, css="form-control"):
    return field.as_widget(attrs={"class": css})


@register.filter
def add_class_req_autofoc(field, css="form-control"):
    return field.as_widget(
        attrs={
            "class": css,
            "required": "",
            "autofocus": "",
        }
    )

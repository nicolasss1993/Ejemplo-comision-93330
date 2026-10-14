from django import forms, template

register = template.Library()


@register.filter
def bootstrap(field):
    """Renderiza un campo de formulario con las clases de Bootstrap que corresponden."""
    widget = field.field.widget
    if isinstance(widget, forms.CheckboxInput):
        clase = "form-check-input"
    elif isinstance(widget, (forms.Select, forms.SelectMultiple)):
        clase = "form-select"
    elif isinstance(widget, forms.ClearableFileInput):
        clase = "form-control"
    else:
        clase = "form-control"
    if field.errors:
        clase += " is-invalid"
    existentes = widget.attrs.get("class", "")
    return field.as_widget(attrs={"class": f"{existentes} {clase}".strip()})


@register.filter
def es_checkbox(field):
    return isinstance(field.field.widget, forms.CheckboxInput)

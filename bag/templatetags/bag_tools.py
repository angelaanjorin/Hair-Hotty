from django import template


register = template.Library()

@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    # If quantity is a dict, extract the value
    if isinstance(quantity, dict):
        quantity = quantity.get('value', 1)  # default to 1 if 'value' is not present
    return price * quantity
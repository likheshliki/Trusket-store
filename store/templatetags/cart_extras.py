from django import template

register = template.Library()

@register.filter
def calc_total(products):
    total = 0
    for product in products:
        try:
            total += float(product.price)
        except Exception:
            pass
    return total

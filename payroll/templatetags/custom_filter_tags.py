from django import template

register = template.Library()


@register.filter
def currency_filter(value):
    """Outputs comma separated rounded off figure"""
    number = float(value)
    rounded_number = round(number)
    integer_number = int(rounded_number)
    return "{:,}".format(integer_number)


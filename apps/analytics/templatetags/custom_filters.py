from django import template
import math 

register = template.Library()

@register.filter

def formatNumbers(value):
    digits = math.floor(math.log10(int(value))) + 1
    label, divisor = '', 0
    if (7 <= digits < 10):
        label = 'M'
        divisor = 1e6
    elif (10 <= digits < 13):
        label = 'B'
        divisor = 1e9
    elif (digits >= 13):
        label = 'T'
        divisor = 1e12
    else:
        label = 'K'
        divisor = 1e3
    number = value / divisor
    return f'{math.floor(number * 100) / 100}{label}'
    
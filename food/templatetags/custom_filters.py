from django import template

register = template.Library()


def divide(value, arg):
    try:
        return float(value) / float(arg)
    except (ValueError, ZeroDivisionError):
        return None


def multiply(value, arg):
    return value * arg


def capitalize(value):
    try:
        if value and isinstance(value, str):
            return value.capitalize()
    except ValueError:
        return None


def subtract(value, arg):
    return round(value - arg)


def round_value(value):
    return round(value)


register.filter('divide', divide)
register.filter('multiply', multiply)
register.filter('capitalize', capitalize)
register.filter('subtract', subtract)
register.filter('round_value', round_value)

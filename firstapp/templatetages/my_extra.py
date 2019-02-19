from django import template


#my custom filter
register = template.Library()


@register.filter(name='cut')
def cut(value, arg):
    """"
    This cut out all value of "arg" from the string!
    """
    return value.replace(arg, '')

# register.filter('cut', cut)

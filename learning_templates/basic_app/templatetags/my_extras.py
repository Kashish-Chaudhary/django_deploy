# this file is creating the custom filters that the used can use in the file




from django import template
register = template.Library()
@register.filter(name='cut')
def cut(value,arg):
    """
    this cuts out all values of "arg " from the string

    """
    return value.replace(arg,'')
#register.filter('cut',cut)    # register the filter cut in the template Library
#second method tho register

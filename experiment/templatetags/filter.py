from django import template

register=template.Library()

def cut(value,arg):
    "remove all values of args from the given string"
    return value.replace(arg,'')

register.filter('cut',cut)

@register.filter(name='lower')  #name缺省值为函数名
def lower(value):
    "convert a string into all lowercase"
    return value.lower()


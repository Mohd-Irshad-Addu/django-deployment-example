from django import template

register = template.Library()#here register is an object
@register.filter(name='cut_this')

def cut(value,arg):
    """
        This cuts out all values of arg from the string!
    """
    return value.replace(arg,'')

#register.filter('cut',cut)#we have another method to use this line that we use with decorator on the third line with @2 symbole

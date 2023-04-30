from django import template

register=template.Library()

def swap(value):
    return value.swapcase()

@register.filter(name='replacing')
def replace(value, arg):

    # for i in range(len(value)):
    #     if value[i:i+len(arg)]==arg:
    #         x=value.replace(arg, '')
    # return x

    return value.replace(arg, '')

@register.filter()
def count(value, arg):
    c=0
    for i in range(len(value)):
        if value[i:i+len(arg)]==arg:
            c+=1
    return c




register.filter('swap', swap)
# register.filter('replace', replace)
#this file is to create your own custom teplate tags
#create a folder>templatestags>create __init__.p file in it
#create your template rendering file and create your tags here
#from blog.templatetags import extras is to add in vies.py to use custom templates tags
#{% load (template_tag_filename) %} is need to add at template file where u want use custom template tags
#__init__.py to declare here templatetags as a package

from django import template

register=template.Library()
@register.filter(name='get_val')
def get_val(dict,key):
    return dict.get(key)
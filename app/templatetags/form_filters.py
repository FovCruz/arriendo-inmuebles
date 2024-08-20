from django import template

register = template.Library()

@register.filter(name='add_class')
def add_class(value, arg):

    return value.as_widget(attrs={'class': arg})



# se debe agregar en los templates {% load form_filters %}

#Modificar Perfil
#registro
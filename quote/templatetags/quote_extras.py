from django import template
from django.contrib.auth.models import Group

register = template.Library()

@register.filter(name='is_in_testing_group')
def is_in_testing_group(user):
    group = Group.objects.get(name='Testing')
    return True if group in user.groups.all() else False

# def is_in_group(user, group_name):
#     group = Group.objects.get(name=group_name)
#     return True if group in user.groups.all() else False

#register.filter("is_in_group", is_in_group)
from blog.models import Author
from django import template

register = template.Library()


@register.filter
def is_author(given_user):
    author = Author.objects.filter(user=given_user).exists()
    if author:
        return True
    else:
        return False

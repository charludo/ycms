from django.template.defaulttags import register


@register.filter
def get_item(dictionary, key):
    """
    Helper function for getting a dictionary item
    """
    return dictionary.get(key, "")

from django.template.defaulttags import register


@register.filter
def get_item(dictionary, key):
    """
    Helper function for getting a dictionary item
    """
    return dictionary.get(key, "")


@register.filter(name="times")
def times(number):
    """
    Helper function for getting a range of numbers
    """
    return range(number)

from django import template

register = template.Library()

@register.simple_tag
def get_path(path, string):
    if string in path:
        return path
    else:
        split_path = path.split('/')
        current_code = split_path[1]
        full_path = path.replace(f'/{current_code}/',f'/{string}/')
        return full_path
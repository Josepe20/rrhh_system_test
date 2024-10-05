from flask import abort

def get_object_or_404(object, message="Resource not found"):
    """
    Verifica si el objeto existe, si no, devuelve un 404.
    """
    if not object:
        abort(404, description=message)
    return object


def get_list_or_404(object_list, message="Resource not found"):
    """
    Verifica si la lista no está vacía, si está vacía, devuelve un 404.
    """
    if not object_list:
        abort(404, description=message)
    return object_list
"""
A FAILING TEST
"""                                 #se le agrega al final para con un valor vacio
def get_formatted_name(first, last, middle = ""):
    """Generetad a neatly formatted full name"""
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()
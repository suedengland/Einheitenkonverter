import functools

def value_formatter(func):
    """
    Dekorator, der eine Gleitkommazahl von einer Funktion entgegen nimmt
    und sie in Abhaengigkeit ihrer Groesse in Exponential- oder Dezimalschreibweise zurueckgibt.
    """
    @functools.wraps(func)
    def format_value(*args, **kwargs):
        val = float(func(*args, **kwargs))

        if abs(val) >= 1e4:
            return f'{val:.3g}'
        return str(val)

    return format_value
import functools

def value_formatter(f_py=None, decimals=None):
    assert callable(f_py) or f_py is None
    def _decorator(func):
        """
        Dekorator, der eine Gleitkommazahl von einer Funktion entgegen nimmt
        und sie in Abhaengigkeit ihrer Groesse in Exponential- oder Dezimalschreibweise zurueckgibt.
        """
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            val = float(func(*args, **kwargs))

            if abs(val) >= 1e4:
                return f'{val:.3g}'
            elif abs(val) < 1e-2:
                return f'{val:.3g}'
            return f'{val:.{decimals}f}' if decimals else str(val)

        return wrapper
    return _decorator(f_py) if callable(f_py) else _decorator
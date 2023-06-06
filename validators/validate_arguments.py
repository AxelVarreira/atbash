from types import NoneType


def validate_arguments(k, a, f):
    if type(k) is NoneType: raise ValueError('None param was passed')
    if type(a) is NoneType: raise ValueError("None param was passed")
    if type(f) is NoneType: raise ValueError("None param was passed")

    if not f.__contains__(".txt"):
        raise ValueError("Invalid file")
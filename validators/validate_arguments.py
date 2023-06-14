from types import NoneType


def validate_arguments(a, f):
    if type(a) is NoneType: raise ValueError("No action was passed")
    if type(f) is NoneType: raise ValueError("No file was passed")

    # extension of file verify
    if not f.__contains__(".txt"):
        raise ValueError("Invalid file", f)

    #action verify
    if a != 'encrypt' and a != 'decrypt':
        raise ValueError("Invalid action ", a)
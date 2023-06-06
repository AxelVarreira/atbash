from types import NoneType


def validate_arguments(k, a, f):
    if type(k) is NoneType: raise ValueError('None param was passed')
    if type(a) is NoneType: raise ValueError("None param was passed")
    if type(f) is NoneType: raise ValueError("None param was passed")

    # Verify if the extension of file
    if not f.__contains__(".txt"):
        raise ValueError("Invalid file", f)

    # key verify
    if k.__contains__(".txt"):
        raise ValueError("Invalid key", k)

    result = bytearray(k.encode('utf-8'))
    if len(result) < 4 or len(result) > 56:
        raise ValueError("The key is invalid", k)

    #action verify
    if a != 'encrypt' and a != 'decrypt':
        raise ValueError("Invalid action ", a)
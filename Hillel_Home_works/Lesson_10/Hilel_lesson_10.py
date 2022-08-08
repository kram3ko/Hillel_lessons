import functools


class UnexpectedTypeException(Exception):
    """Return type is not as expected."""


def expected(*types: type):
    def decorator(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            result = func(*args, **kwargs)
            if not isinstance(result, types):
                raise UnexpectedTypeException(
                    f'return type {type(result)} is not as expected: {types}')

        return inner

    return decorator


@expected(int,str,tuple)
def check_type(type):
    return type

check_type(123)
check_type((1,3,"{}"))
check_type({})

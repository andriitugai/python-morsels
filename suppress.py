from functools import wraps


class suppress(object):

    def __init__(self, *exceptionTypes):
        self.exceptionTypes = exceptionTypes

    def __call__(self, function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            with self:
                return function(*args, **kwargs)

        return wrapper

    def __enter__(self):
        return self

    def __exit__(self, exception_type, exception, traceback):
        self.exception = exception
        self.traceback = traceback
        return isinstance(exception, self.exceptionTypes)


@suppress(TypeError)
def len_or_none(thing):
    return len(thing)


with suppress(ValueError, NameError):
    print("Hi!")
    print("It's nice to meet you,", name)
    a = int('Hello')
    print("Goodbye!")

with suppress(ValueError, TypeError):
    x = int('hello')

with suppress(ValueError, TypeError):
    x = int(None)

print(len_or_none('hello'))
print(len_or_none(24))
print(len_or_none([1, 2, 3, 4, 5, 6, 7, 8]))


print('done')

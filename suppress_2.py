from contextlib import contextmanager


@contextmanager
def suppress(*exception_type):
    try:
        yield
    except exception_type:
        pass


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

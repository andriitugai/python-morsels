import functools
from collections import namedtuple

NO_RETURN = object()


def record_calls(func):

    Call = namedtuple('Call', ['args', 'kwargs', 'return_value', 'exception'])

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.call_count += 1
        try:
            result = func(*args, **kwargs)
            exc = None
        except Exception as e:
            exc = e
            result = NO_RETURN

        wrapper.calls.append(Call(args, kwargs, result, exc))
        if exc:
            raise exc

        return result

    wrapper.call_count = 0
    wrapper.calls = []
    return wrapper


@record_calls
def greet(name="world"):
    """Greet someone by their name."""
    print(f"Hello {name}")


@record_calls
def cube(n):
    return n ** 3


def main():
    greet("Trey")
    print(greet.call_count)
    import pydoc
    print(pydoc.render_doc(greet))

    print(greet.calls[0].args)
    # ('Trey',)
    print(greet.calls[0].kwargs)
    # {}
    greet(name="Trey")
    print(greet.calls[1].args)
    print(greet.calls[1].kwargs)
    # {'name': 'Trey'}


    cube(3)
    # 27
    print(cube.calls)
    # [Call(args=(3,), kwargs={}, return_value=27, exception=None)]

    cube(None)
    print(cube.calls)


if __name__ == '__main__':
    main()



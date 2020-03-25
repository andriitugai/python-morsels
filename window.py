import collections


def window(itrbl, n, *, fillvalue=None):
    if n <= 0:
        return []

    d = collections.deque(maxlen=n)
    sent = False

    for item in itrbl:
        d.append(item)
        if len(d) == d.maxlen:
            sent = True
            yield tuple(d)

    if not sent:
        yield tuple(d) + (fillvalue,) * (n-len(d))


def main():
    numbers = [1, 2, 3, 4, 5, 6]
    # print(next(window(numbers, 3)))
    print(next(window(numbers, 12)))
    print(next(window(numbers, 0)))
    print(next(window([], 4)))
    print(*window(numbers, 2))
    print(*window(numbers, 3))
    #
    # squares = (n**2 for n in numbers)
    # print(window(squares, 4))


if __name__ == '__main__':
    main()




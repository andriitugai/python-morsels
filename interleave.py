import itertools

sentinel = object()

def interleave(*itrs):

    # flatten the sequence:
    for tpl in itertools.zip_longest(*itrs, fillvalue=sentinel):
        for itm in tpl:
            if itm is not sentinel:
                yield itm



def main():
    numbers = [1, 2, 3, 4]
    print(*interleave([1, 2, 3], [4, 5, 6, 7, 8]))
    # [1, 5, 2, 6, 3, 7, 4, 8]
    print(*interleave([1, 2, 3], [4, 5], [6, 7, 8, 9]))
    # [1, 1, 2, 4, 3, 9, 4, 16]

    # bonus 1
    i = interleave([1, 2, 3, 4], [5, 6, 7, 8])
    print(next(i))
    # 1
    print(list(i))
    # [5, 2, 6, 3, 7, 4, 8]

    in1 = [1, 2, 3]
    squares = (n ** 2 for n in in1)
    output = interleave(squares, squares)
    print(next(output))
    print(next(output))
    print(next(squares))


if __name__ == '__main__':
    main()

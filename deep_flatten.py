
def deep_flatten(seq):
    flat = []
    for item in seq:
        try:
            _ = iter(item)
            deep_flatten(item)
        except TypeError as te:
            flat.append(item)

    return flat


if __name__ == '__main__':
    # l1 = [1, 2, 3, 4]
    l1 = [[(1, 2), (3, 4)], [(5, 6), (7, 8)]]
    print(deep_flatten(l1))

    # l1 = [[1, [2, 3]], 4, 5]
    # print(deep_flatten(l1))

# https://www.pythonmorsels.com/exercises/e9219d8a7f7c4ef189b9c6b04ff98a5b/

import itertools
import collections


class CyclicList_(object):
    def __init__(self, itrbl):
        self._itrbl = list(itrbl)

    def __iter__(self):
        return itertools.cycle(self._itrbl)

    def __len__(self):
        return len(self._itrbl)

    def append(self, other):
        self._itrbl.append(other)

    def pop(self, idx=-1):
        return self._itrbl.pop(idx)


class CyclicList(collections.UserList):

    def __iter__(self):
        return itertools.cycle(super(CyclicList, self).__iter__())

    def __getitem__(self, idx):
        if isinstance(idx, slice):
            start = idx.start or 0
            stop = idx.stop
            if stop is None:
                if start >= 0:
                    stop = super(CyclicList, self).__len__()
                else:
                    stop = 0
            return [
                super(CyclicList, self).__getitem__(i % super(CyclicList, self).__len__())
                for i in range(start, stop, idx.step or 1)
            ]

        return super(CyclicList, self).__getitem__(idx % super(CyclicList, self).__len__())

    def __setitem__(self, idx, val):
        super(CyclicList, self).__setitem__(idx % super(CyclicList, self).__len__(), val)


def main():
    my_list = CyclicList([1, 2, 3])
    my_list.append(4)
    my_list.pop(1)

    for i, n in enumerate(my_list):
        print(n)
        if i > 8:
            break

    print(list(itertools.islice(my_list, 5)))
    # print(len(my_list))
    # print(my_list.pop())
    # print(len(my_list))

    print(my_list[8])
    print(my_list[-5])
    # print(my_list[:8])

    numbers = CyclicList([1, 2, 3, 4, 5])
    print(numbers[:7])      # [1, 2, 3, 4, 5, 1, 2])
    print(numbers[-3:])     # [3, 4, 5])
    print(numbers[-10:0])   # [1, 2, 3, 4, 5, 1, 2, 3, 4, 5])
    print(numbers[-1:9])    # [5, 1, 2, 3, 4, 5, 1, 2, 3, 4])
    print(numbers[:])       # [1, 2, 3, 4, 5])


if __name__ == '__main__':
    main()

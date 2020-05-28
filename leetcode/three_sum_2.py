
def threeSum(A):
    '''
    :type A: list of int
    :rtype: list of list of int
    '''

    def twoSum(arr, target):
        """
        :type arr: list of int
        :type target: int
        :rtype: list of unique pairs
        """
        if not arr or len(arr) < 2:
            return []

        additions = {}
        result = []

        idx = 0
        while idx < len(arr):
            wanted = target - arr[idx]
            if wanted in additions:
                result.append([arr[idx], arr[additions[wanted]]])
            else:
                additions[arr[idx]] = idx

            idx += 1

        return result

    if not A or len(A) < 3:
        return []

    result = []
    idx = 0
    targets_done = set()

    while idx < len(A) - 1:
        target = 0 - A[idx]
        if target not in targets_done:
            add_pairs = twoSum(A[idx + 1:], target)
            if add_pairs:
                result.extend(
                    [[A[idx], *arr] for arr in add_pairs]
                )
        idx += 1

    return result


def main():

    print(threeSum([-3, -1, 1, 0, 2, 10, -2, 8]))


if __name__ == '__main__':
    main()

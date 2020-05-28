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


def main():
    print(twoSum([4, 2, -1, 3, 0, 5, 1], 6))


if __name__ == '__main__':
    main()

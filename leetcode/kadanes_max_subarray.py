def max_subarray(arr):
    """
    Returns max sum of subarray for given array.
    :param arr: list(int)
    :return: int
    """
    if not arr:
        return 0

    global_max = local_max = arr[0]
    for idx in range(1,len(arr)):
        local_max = max(local_max+arr[idx], arr[idx])
        global_max = max(local_max, global_max)

    return global_max


def max_cycle_subbaray(arr):
    """
    Returns max sum of subarray for "cycled" array
    :param arr: list(int)
    :return: int
    """
    if not arr:
        return 0

    global_max = global_min = arr[0]
    local_max = local_min = arr[0]
    total = arr[0]

    for idx in range(1,len(arr)):
        local_max = max(local_max+arr[idx], arr[idx])
        global_max = max(global_max, local_max)

        local_min = min(local_min+arr[idx], arr[idx])
        global_min = min(global_min, local_min)

        total += arr[idx]

    if global_min == total:
        return global_max
    else:
        return max(global_max, total - global_min)




def main():
    a = [-2, 3, 2, -1]
    print(max_subarray(a))

    b = [5, -3, 5]
    print(max_cycle_subbaray(b))


if __name__ == '__main__':
    main()


def checkStraightLine(coordinates):
    """
    :type coordinates: List[List[int]]
    :rtype: bool
    """
    if len(coordinates) == 2:
        return True

    x0 = coordinates[0][0]
    y0 = coordinates[0][1]

    dx1 = coordinates[1][0] - coordinates[0][0]
    dy1 = coordinates[1][1] - coordinates[0][1]

    return all([(c[1]-y0) * dx1 == (c[0]-x0) * dy1 for idx, c in enumerate(coordinates) if idx > 1])


def main():
    print(checkStraightLine([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]))
    print(checkStraightLine([[1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]]))


if __name__ == '__main__':
    main()

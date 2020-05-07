def checkOverlap(radius, x_center, y_center, x1, y1, x2, y2):
    """
    :type radius: int
    :type x_center: int
    :type y_center: int
    :type x1: int
    :type y1: int
    :type x2: int
    :type y2: int
    :rtype: bool
    """
    x1a = x1 - x_center
    x2a = x2 - x_center
    y1a = y1 - y_center
    y2a = y2 - y_center

    if x1a <= 0 <= x2a:
        return y1a <= radius and y2a >= -radius

    if y1a <= 0 <= y2a:
        return x1a <= radius and x2a >= -radius

    rsq = radius * radius
    return any([x * x + y * y <= rsq for x in (x1a, x2a) for y in (y1a, y2a)])


def main():
    print("Overlapped: ", checkOverlap(1415, 807, -784, -733, 623, -533, 1005))


if __name__ == '__main__':
    main()


def print_pascal(rows):
    pascal = {}
    def get_pascal(i,j):
        if j > i:
            return 0
        if (i,j) in pascal:
            return pascal[i,j]
        if i == 0 or j == 0 or j == i:
            pascal[i, j] = 1
        else:
            pascal[i,j] = get_pascal(i-1, j-1) + get_pascal(i-1, j)

        return pascal[i,j]

    for i in range(rows):
        print(' ' * (rows - i), end = '')
        for j in range(i+1):
            print(get_pascal(i,j), end=' ')
        print()

def main():
    print_pascal(9)


if __name__ == '__main__':
    main()


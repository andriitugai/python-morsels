from itertools import zip_longest

def add(*arg):
    
    sentinel = object()
    try:
        result = ([[ sum(c) for c in zip_longest(*rows, fillvalue=sentinel)] for rows in zip_longest(*arg, fillvalue=[])])
    except TypeError:
        raise ValueError("Given matrices are not the same size.")
    
    return result

def add_m(*arg):
    
    try:
        return [
            [sum(c) for c in zip_longest(*rows)] 
            for rows in zip_longest(*arg)
        ]
    except TypeError as err:
        raise ValueError("Given matrices are not the same size.") from err
    
    
def main():
    matrix1 = [[1, -2], [-3, 4]]
    matrix2 = [[2, -1], [0, -1]]
    matrix3 = [[-3, 3], [3, -3]]

    matrix4 = [[2, -1], [0, -1], [5, -5]]
    matrix5 = [[2, -1], [0]]


    res = add_m(matrix1, matrix2, matrix3)
    print(res)

    res = add_m(matrix1, matrix5)
    print(res)

    # res = add_m(matrix1)
    # print(res)

    # res = add_m()
    # print(res)


if __name__ == '__main__':
    main()
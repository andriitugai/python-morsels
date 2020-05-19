import linked_lists.my_linked_list as ll

def main():
    a = [1, 2, 3, 4, 5, 'Hello', 6]

    my_ll = ll.LinkedList().build_from_iterbl(a)
    print(my_ll)

    ll2 = ll.LinkedList().reverse_iterative(my_ll)
    print(ll2)

    print(my_ll)
    ll3 = ll.LinkedList().reverse_recursive(my_ll)
    print(ll3)


if __name__ == '__main__':
    main()

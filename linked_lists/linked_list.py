import linked_lists.my_linked_list as ll

def get_middle(head):
    """
    returns middle element of the linked list
    :param head: ll.Node
    :return: ll.Node
    """
    if not head or not head.next:
        return head

    fast = head
    slow = head
    while fast.next:
        fast = fast.next
        if fast.next is None:
            print("even!")
            return slow
        fast = fast.next
        slow = slow.next

    return slow

def isPalindrome(head):
    """
    :type head: ListNode
    :rtype: bool
    """
    def reverse(fead):
        if not fead or not fead.next:
            return fead
        pre = None
        cur = fead

        while cur.next:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt

        cur.next = pre

        return cur

    if not head or not head.next:
        return True
    # get the middle element
    fast = head
    slow = head
    while fast.next:
        fast = fast.next
        if fast.next is None:
            is_odd = False
            break
        fast = fast.next
        slow = slow.next
    # slow.next points to the haead of the second half
    gead = slow.next
    # Reverse in-place the second half
    gead = reverse(gead)

    gp = gead
    hp = head
    is_palindrome = True
    while gp.next:
        if hp.val != gp.val:
            is_palindrome = False
        hp = hp.next
        gp = gp.next

    if hp.val != gp.val:
        is_palindrome = False

    reverse(gead)

    return is_palindrome


def main():
    a = [1, 2, 3, 4, 5, 3, 2, 1]

    my_ll = ll.LinkedList().build_from_iterbl(a)
    print(my_ll)

    ll2 = ll.LinkedList().reverse_iterative(my_ll)
    print(ll2)
    #
    # print(my_ll)
    # ll3 = ll.LinkedList().reverse_recursive(my_ll)
    # print(ll3)
    #
    # print(get_middle(ll3.head).val)

    print(isPalindrome(my_ll.head))


if __name__ == '__main__':
    main()

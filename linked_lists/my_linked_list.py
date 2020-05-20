class Node(object):
    def __init__(self, val=None):
        self.val = val
        self.next = None


class LinkedList(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None

    @staticmethod
    def build_from_iterbl(iterbl):
        ll = LinkedList()
        for item in iterbl:
            ll.addAtTail(item)

        return ll

    @staticmethod
    def reverse_iterative(llist):
        prev = None
        curr = llist.head

        while curr is not None:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        llist.head = prev
        return llist


    @staticmethod
    def reverse_recursive(llist):
        def reverse(head):
            if not head or not head.next:
                return head
            new_head = reverse(head.next)
            head.next.next = head
            head.next = None

            return new_head

        llist.head = reverse(llist.head)
        return llist

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if index < 0:
            return -1

        n = 0
        pointer = self.head
        while pointer.next and n < index:
            pointer = pointer.next
            n += 1

        if n != index:
            return -1
        else:
            return pointer.val

    def getNode(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if index < 0:
            return -1

        n = 0
        pointer = self.head
        while pointer.next and n < index:
            pointer = pointer.next
            n += 1

        if n != index:
            return -1
        else:
            return pointer

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list.
        After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: None
        """
        if not self.head:
            self.head = Node(val)
            return

        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node


    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: None
        """
        if not self.head:
            self.head = Node(val)
            return

        pointer = self.head
        while pointer.next:
            pointer = pointer.next

        pointer.next = Node(val)

    def addNodeAtTail(self, node):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: None
        """
        if not self.head:
            self.head = node
            return

        pointer = self.head
        while pointer.next:
            pointer = pointer.next

        pointer.next = node

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list.
        If index equals to the length of linked list, the node will be appended to the end of linked list.
        If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: None
        """
        if index < 0:
            return

        if index == 0:
            new_node = Node(val)
            new_node.next = self.head
            self.head = new_node

        n = 0
        pointer = self.head
        while pointer.next and n < index - 1:
            pointer = pointer.next
            n += 1

        if n != index - 1:
            return

        new_node = Node(val)
        new_node.next = pointer.next

        pointer.next = new_node

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: None
        """
        if index < 0:
            return

        if index == 0:
            self.head = self.head.next
            return

        pointer = self.head
        for i in range(index - 1):
            pointer = pointer.next
            if pointer is None:
                break

        # If position is more than number of nodes
        if pointer is None:
            return
        if pointer.next is None:
            return

        # Node temp.next is the node to be deleted
        # store pointer to the next of node to be deleted
        nxt = pointer.next.next

        pointer.next = nxt


    def __repr__(self):
        result = str(self.head.val)

        pointer = self.head
        while pointer and pointer.next:
            pointer = pointer.next
            result += (" -> " + str(pointer.val))

        return result

    def print(self):
        pointer = self.head
        if not pointer:
            return

        print(pointer.val, sep='', end='')
        while pointer.next:
            pointer = pointer.next
            print('->',pointer.val, sep='', end='')


class Solution(object):
    # Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
    #
    # To represent a cycle in the given linked list, we use an integer pos which represents the position
    # (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.
    #
    # Note: Do not modify the linked list.
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None

        path = {}
        pointer = head
        position = 0

        while pointer.next:
            if pointer.next in path:
                return path[pointer.next]
            else:
                path[pointer] = pointer
            pointer = pointer.next

            position += 1

        return None

    # Write a program to find the node at which the intersection of two singly linked lists begins.
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA:
            return None
        else:
            count_a = 1
            pointer = headA
            while pointer.next:
                pointer = pointer.next
                count_a += 1

        if not headB:
            return None
        else:
            count_b = 1
            pointer = headB
            while pointer.next:
                pointer = pointer.next
                count_b += 1

        if count_a < count_b:
            headA, headB = headB, headA
            count_a, count_b = count_b, count_a

        # A is not shorter than B
        delta = count_a - count_b
        pointer_a = headA
        pointer_b = headB

        while delta > 0:
            if not pointer_a:
                return None
            pointer_a = pointer_a.next
            delta -= 1

        while True:
            if pointer_a == pointer_b:
                return pointer_a
            pointer_a = pointer_a.next
            pointer_b = pointer_b.next
            if pointer_a is None or pointer_b is None:
                break

        return None


def main():
    a = LinkedList()

    a.addAtHead(2)
    # a.deleteAtIndex(1)
    # a.addAtHead(2)
    # a.addAtHead(7)
    # a.addAtHead(3)
    # a.addAtHead(2)
    # a.addAtHead(5)
    a.addAtTail(5)
    a.addAtTail(6)
    a.addAtTail(7)
    a.addAtTail(8)
    a.addAtTail(9)
    # a.get(5)
    # print(a)
    # a.deleteAtIndex(6)
    # a.deleteAtIndex(4)
    #
    print(a)

    node_2 = a.getNode(2)
    print(node_2.val)
    a.addNodeAtTail(node_2)
    # a.print()

    print(Solution().detectCycle(a.head) == node_2)


if __name__ == '__main__':
    main()

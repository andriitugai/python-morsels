class MyLinkedList(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.val = None
        self.next = None

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if index < 0:
            return -1

        n = 0
        pointer = self
        while pointer.next is not None and n < index:
            pointer = pointer.next
            n += 1

        if n != index:
            return -1
        else:
            return pointer.val

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion,
        the new node will be the first node of the linked list.
        :type val: int
        :rtype: None
        """
        new_node = MyLinkedList()
        new_node.val = val
        new_node.next = self
        self = new_node

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: None
        """
        pointer = self
        while pointer.next is not None:
            pointer = pointer.next

        new_node = MyLinkedList()
        new_node.val = val

        pointer.next = new_node

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: None
        """
        if index < 0:
            return

        n = 0
        pointer = self
        while pointer.next is not None and n < index:
            pointer = pointer.next
            n += 1

        if n != index:
            return

        new_node = MyLinkedList()
        new_node.val = val
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

        n = 0
        pointer = self
        while pointer.next is not None and n < index:
            pointer = pointer.next
            n += 1

        if n != index:
            return

        pointer.next = pointer.next.next

    def __repr__(self):
        result = str(self.val)

        pointer = self
        while True:
            if pointer.next is None:
                break
            pointer = pointer.next
            result += (" -> " + str(pointer.val))

        return result



def main():
    a = MyLinkedList()

    a.addAtHead(3)

    print(a)


if __name__ == '__main__':
    main()

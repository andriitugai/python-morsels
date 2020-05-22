# https://leetcode.com/explore/learn/card/linked-list/213/conclusion/1225/

# You are given a doubly linked list which in addition to the next and previous pointers,
# it could have a child pointer, which may or may not point to a separate doubly linked list.
# These child lists may have one or more children of their own, and so on, to produce a multilevel
# data structure, as shown in the example below.
#
# Flatten the list so that all the nodes appear in a single-level, doubly linked list.
# You are given the head of the first level of the list.

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """

        def flat(head):
            if not head:
                return head
            pointer = head
            while True:
                curr_next = pointer.next

                if pointer.child:
                    child_tail = flat(pointer.child)

                    pointer.next = pointer.child
                    pointer.next.prev = pointer
                    pointer.child = None

                    if curr_next:
                        child_tail.next = curr_next
                        curr_next.prev = child_tail

                if curr_next:
                    pointer = curr_next
                else:
                    return pointer

        flat(head)
        return head

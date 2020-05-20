# https://leetcode.com/explore/learn/card/linked-list/213/conclusion/1229/

# A linked list is given such that each node contains an additional random pointer
# which could point to any node in the list or null.
#
# Return a deep copy of the list.
#
# The Linked List is represented in the input/output as a list of n nodes.
# Each node is represented as a pair of [val, random_index] where:
#
# val: an integer representing Node.val
# random_index: the index of the node (range from 0 to n-1) where random pointer points to, or null if it does not point to any node.

"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return head

        if not head.next:
            new_node = Node(head.val)
            if head.random:
                new_node.random = new_node
            return new_node

        # interweave the nodes of the old and copied lists:
        pointer = head
        while True:
            # create a copy of the Node
            new_node = Node(pointer.val)
            new_node.next = pointer.next
            pointer.next = new_node

            if new_node.next is None:
                break
            else:
                pointer = new_node.next

        # copy "random" connections:
        pointer = head
        while True:
            if pointer.random:
                pointer.next.random = pointer.random.next
            pointer = pointer.next.next

            if not pointer:
                break

        # split lists:
        p0 = head
        new_head = head.next
        p1 = new_head
        while True:
            p0.next = p0.next.next
            p1.next = p1.next.next

            p0 = p0.next
            p1 = p1.next

            if p1.next is None:
                p0.next = None
                break

        return new_head

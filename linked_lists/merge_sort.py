# https://leetcode.com/problems/sort-list/
#
# Sort a linked list in O(n log n) time using constant space complexity.
#
# Example 1:
# Input: 4->2->1->3
# Output: 1->2->3->4
# Example 2:
# Input: -1->5->3->4->0
# Output: -1->0->3->4->5

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # base case
        if head is None or head.next is None:
            return head

        # get a middle of the list:
        slow = head
        fast = head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next

        # slow points to a middle of the list.
        # divide list at this point:
        right_list = slow.next
        slow.next = None

        left_list = self.sortList(head)
        right_list = self.sortList(right_list)

        return self.merge_sorted_lists(left_list, right_list)

    def merge_sorted_lists(self, h1, h2):
        # base cases:
        if h1 is None:
            return h2

        if h2 is None:
            return h1

        # recursive
        if h1.val < h2.val:
            result = h1
            result.next = self.merge_sorted_lists(h1.next, h2)
        else:
            result = h2
            result.next = self.merge_sorted_lists(h1, h2.next)

        return result


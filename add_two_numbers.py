# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        list = []
        cur_elem = self
        while True:
            list.append(str(cur_elem.val))
            cur_elem = cur_elem.next
            if cur_elem is None:
                break
        return '->'.join(list)


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode()
        cur_elem = result
        cur1 = l1
        cur2 = l2
        rest = 0
        while True:
            summa = (cur1.val if cur1 else 0) + (cur2.val if cur2 else 0) + rest
            cur_elem.val = summa % 10
            rest = summa // 10

            cur1 = cur1.next if cur1 else None
            cur2 = cur2.next if cur2 else None

            if not cur1 and not cur2:
                break

            cur_elem.next = ListNode()
            cur_elem = cur_elem.next

        if rest > 0:
            cur_elem.next = ListNode(rest)

        return result


def main():
    l1 = ListNode(2, next=ListNode(4, next=ListNode(3)))
    l2 = ListNode(7, next=ListNode(0, next=ListNode(8)))

    print(l1)
    print(l2)

    print(Solution().addTwoNumbers(l1, l2))


if __name__ == '__main__':
    main()




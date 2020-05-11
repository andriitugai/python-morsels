# https://leetcode.com/problems/count-and-say/

# The count-and-say sequence is the sequence of integers with the first five terms as following:
#
# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.
#
# Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.
# You can do so recursively, in other words from the previous member read off the digits,
# counting the number of digits in groups of the same digit.
#
# Note: Each term of the sequence of integers will be represented as a string.

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """

        if n == 1:
            return "1"
        else:
            nstr = self.countAndSay(n - 1)
            cur_char = nstr[0]
            count = 1
            idx = 1
            result = ""
            while idx < len(nstr):
                if cur_char == nstr[idx]:
                    count += 1
                else:
                    result += str(count * 10 + int(cur_char))
                    cur_char = nstr[idx]
                    count = 1

                idx += 1

            result += str(count * 10 + int(cur_char))
            return result


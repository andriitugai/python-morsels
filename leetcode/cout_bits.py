# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/537/week-4-may-22nd-may-28th/3343/

# Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num
# calculate the number of 1's in their binary representation and return them as an array.
#
# Example 1:
# Input: 2
# Output: [0,1,1]

# Example 2:
# Input: 5
# Output: [0,1,1,2,1,2]
# Follow up:
#
# It is very easy to come up with a solution with run time O(n*sizeof(integer)).
# But can you do it in linear time O(n) /possibly in a single pass?
# Space complexity should be O(n).
# Can you do it like a boss? Do it without using any builtin function
# like __builtin_popcount in c++ or in any other language.


class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        if num == 0:
            return [0]

        result = [0, 1]
        curr = 2
        power = 2

        while curr <= num:
            if curr >= power * 2:
                power *= 2
            result.append(1 + result[curr - power])
            curr += 1

        return result

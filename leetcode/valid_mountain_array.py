# https://leetcode.com/explore/featured/card/fun-with-arrays/527/searching-for-items-in-an-array/3251/

# Given an array A of integers, return true if and only if it is a valid mountain array.
#
# Recall that A is a mountain array if and only if:
# A.length >= 3
# There exists some i with 0 < i < A.length - 1 such that:
# A[0] < A[1] < ... A[i-1] < A[i]
# A[i] > A[i+1] > ... > A[A.length - 1]

class Solution(object):
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if not A or len(A) < 3:
            return False

        idx = 0
        while idx < len(A) - 1 and A[idx] < A[idx + 1]:
            idx += 1

        if idx == 0 or idx == len(A) - 1:
            return False

        while idx < len(A) - 1 and A[idx] > A[idx + 1]:
            idx += 1

        return idx == len(A) - 1

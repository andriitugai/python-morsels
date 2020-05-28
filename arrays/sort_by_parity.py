# https://leetcode.com/explore/featured/card/fun-with-arrays/511/in-place-operations/3260/

# Given an array A of non-negative integers, return an array consisting of all the even elements of A,
# followed by all the odd elements of A.
#
# You may return any answer array that satisfies this condition.
#
# Example 1:
# Input: [3,1,2,4]
# Output: [2,4,3,1]
# The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.#
# Note:
# 1 <= A.length <= 5000
# 0 <= A[i] <= 5000

class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        if not A:
            return A

        p_odd = 0
        p_even = len(A) - 1

        while p_odd < p_even:
            if A[p_odd] % 2 == 1 and A[p_even] % 2 == 0:
                A[p_odd], A[p_even] = A[p_even], A[p_odd]
                p_odd += 1
                p_even -= 1
            elif A[p_odd] % 2 != 1:
                p_odd += 1
            else:
                p_even -= 1

        return A

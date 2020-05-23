# https://leetcode.com/explore/featured/card/may-leetcoding-challenge/537/week-4-may-22nd-may-28th/3338/

# Given two lists of closed intervals, each list of intervals is pairwise disjoint and in sorted order.
#
# Return the intersection of these two interval lists.
#
# (Formally, a closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.
# The intersection of two closed intervals is a set of real numbers that is either empty,
# or can be represented as a closed interval.  For example, the intersection of [1, 3] and [2, 4] is [2, 3].)
#
# Example 1:
# Input: A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]]
# Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
# Reminder: The inputs and the desired output are lists of Interval objects, and not arrays or lists.
#
class Solution(object):
    def intervalIntersection(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        if not A or not B:
            return []

        pa = pb = 0
        result = []

        while pa < len(A) and pb < len(B):

            start = max(A[pa][0], B[pb][0])
            end = min(A[pa][1], B[pb][1])

            if start <= end:
                result.append([start, end])
                if end == A[pa][1]:
                    pa += 1
                if end == B[pb][1]:
                    pb += 1
            else:
                if start == A[pa][0]:
                    pb += 1
                else:
                    pa += 1

        return result
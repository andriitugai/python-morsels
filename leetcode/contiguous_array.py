# https://leetcode.com/explore/featured/card/may-leetcoding-challenge/537/week-4-may-22nd-may-28th/3341/

# Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.
#
# Example 1:
# Input: [0,1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
# Example 2:
# Input: [0,1,0]
# Output: 2
# Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
# Note: The length of the given binary array will not exceed 50,000.

class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        ans = 0
        # count 1s as +1 and 0s as -1
        counts = {1: 1, 0: -1}
        count = 0
        idx = 0

        results = {0: -1}  # map curr count to the first index where it has been reached
        # our count starts at -1 with the result 0
        while idx < len(nums):
            count += counts[nums[idx]]
            if count in results:
                ans = max(ans, idx - results[count])
            else:
                results[count] = idx

            idx += 1

        return ans


class Solution(object):
    """
    Given an array of size n, find the majority element.
    The majority element is the element that appears more than ⌊ n/2 ⌋ times.

    You may assume that the array is non-empty and the majority element always exist in the array.

    Example 1:

    Input: [3,2,3]
    Output: 3
    Example 2:

    Input: [2,2,1,1,1,2,2]
    Output: 2
    """
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import defaultdict

        cnt = defaultdict(int)
        for num in nums:
            cnt[num] += 1

        goal = len(nums) / 2

        for key, value in cnt.items():
            if value > goal:
                return key

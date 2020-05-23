# https://leetcode.com/explore/featured/card/fun-with-arrays/526/deleting-items-from-an-array/3248/
#
# Given a sorted array nums, remove the duplicates in-place such that each element
# appear only once and return the new length.
#
# Do not allocate extra space for another array, you must do this
# by modifying the input array in-place with O(1) extra memory.
#
# Example 1:
# Given nums = [1,1,2],
# Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
# It doesn't matter what you leave beyond the returned length.

# Example 2:
# Given nums = [0,0,1,1,1,2,2,3,3,4],
# Your function should return length = 5, with the first five elements of nums being modified
# to 0, 1, 2, 3, and 4 respectively.
# It doesn't matter what values are set beyond the returned length.

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        fast = 1
        slow = 1
        item = nums[0]
        while fast < len(nums):
            if nums[fast] != item:
                item = nums[fast]
                nums[slow] = item
                slow += 1

            fast += 1

        return slow

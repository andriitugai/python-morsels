# https://leetcode.com/explore/featured/card/fun-with-arrays/526/deleting-items-from-an-array/3247/

# Given an array nums and a value val, remove all instances of that value in-place and return the new length.
#
# Do not allocate extra space for another array, you must do this
# by modifying the input array in-place with O(1) extra memory.
# The order of elements can be changed. It doesn't matter what you leave beyond the new length.
#
# Example 1:
# Given nums = [3,2,2,3], val = 3,
# Your function should return length = 2, with the first two elements of nums being 2.
# It doesn't matter what you leave beyond the returned length.

# Example 2:
# Given nums = [0,1,2,2,3,0,4,2], val = 2,
# Your function should return length = 5, with the first five elements of nums containing 0, 1, 3, 0, and 4.
# Note that the order of those five elements can be arbitrary.
# It doesn't matter what values are set beyond the returned len

# 1st way: move all except val into beginning
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums:
            return 0

        slow = -1
        fast = 0
        while fast < len(nums):
            if nums[fast] != val:
                slow += 1
                nums[slow] = nums[fast]
            fast += 1

        return slow + 1

# 2nd way: swap vals with the last element and decrease the length
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums:
            return 0

        last = len(nums) - 1
        fast = 0
        while nums[last] == val and last > 0:
            last -= 1

        while fast <= last:
            if nums[fast] == val:
                nums[fast], nums[last] = nums[last], nums[fast]
                last -= 1
                while nums[last] == val and last > 0:
                    last -= 1

            fast += 1

        return last + 1


# https://leetcode.com/problems/3sum/

# Given an array nums of n integers, are there elements a, b, c in nums
# such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
#
# Note:
# The solution set must not contain duplicate triplets.
#
# Example:
# Given array nums = [-1, 0, 1, 2, -1, -4],
# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def twoSum(nums, target):

            if len(nums) < 2:
                return None

            result = {}
            additions = {}

            for num in nums:
                if target - num in additions:
                    result[target - num] = additions[target - num]
                else:
                    additions[num] = target - num

            return result

        nums = sorted(nums)

        result = []
        prev = object()

        for idx, num in enumerate(nums):
            if num != prev:
                pairs = twoSum(nums[idx + 1:], 0 - num)
                if pairs:
                    result.extend([[num, a, b] for a, b in pairs.items()])

            prev = num

        return result

def main():
    a = [0,0,0,0]
    print(Solution().threeSum(a))
    a = [-1,0,1,2,-1,-4]
    print(Solution().threeSum(a))



if __name__ == '__main__':
    main()

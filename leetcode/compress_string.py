# https://leetcode.com/problems/string-compression/

# Given an array of characters, compress it in-place.
# The length after compression must always be smaller than or equal to the original array.
# Every element of the array should be a character (not int) of length 1.
# After you are done modifying the input array in-place, return the new length of the array.
#
# Follow up:
# Could you solve it using only O(1) extra space?
#
# Example 1:
# Input:
# ["a","a","b","b","c","c","c"]
# Output:
# Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
# Explanation:
# "aa" is replaced by "a2". "bb" is replaced by "b2". "ccc" is replaced by "c3".
#
# Example 2:#
# Input:
# ["a"]
# Output:
# Return 1, and the first 1 characters of the input array should be: ["a"]
# Explanation:
# Nothing is replaced.

class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        count = 1
        idx = 0
        pointer = 0

        while idx < len(chars):
            if idx + 1 < len(chars) and chars[idx] == chars[idx+1]:
                count += 1
            else:
                chars[pointer] = chars[idx]
                pointer += 1
                if count > 1:
                    for c in str(count):
                        chars[pointer] = c
                        pointer += 1

                count = 1

            idx += 1


        return pointer

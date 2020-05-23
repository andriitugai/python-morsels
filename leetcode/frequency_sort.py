# https://leetcode.com/explore/featured/card/may-leetcoding-challenge/537/week-4-may-22nd-may-28th/3337/

# Given a string, sort it in decreasing order based on the frequency of characters.
#
# Example 1:
#
# Input:
# "tree"
#
# Output:
# "eert"
# Explanation:
# 'e' appears twice while 'r' and 't' both appear once.
# So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return s

        import collections
        freqs = collections.defaultdict(int)
        for c in s:
            freqs[c] += 1
        char_items = sorted(list(freqs.items()), key=lambda item: item[1], reverse=True)
        result = []
        for item in char_items:
            result.extend([item[0]] * item[1])

        return ''.join(result)

from collections import defaultdict


class Solution(object):
    """
    Given a string, find the first
    non-repeating character in it and return it's index.
    If it doesn't exist, return -1.
    """
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = defaultdict(int)
        for ch in s:
            d[ch] += 1

        for idx, ch in enumerate(s):
            if d[ch] == 1:
                return idx

        return -1

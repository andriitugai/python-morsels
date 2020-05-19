#

# Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1.
# In other words, one of the first string's permutations is the substring of the second string.
#
# Example 1:
# Input: s1 = "ab" s2 = "eidbaooo"
# Output: True
# Explanation: s2 contains one permutation of s1 ("ba").
# Example 2:
# Input:s1= "ab" s2 = "eidboaoo"
# Output: False
#
# Note:
# The input strings only contain lower case letters.
# The length of both given strings is in range [1, 10,000].
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s2: str
        :type s1: str
        :rtype: bool
        """
        if not s1:
            return True
        if not s2 or len(s2) < len(s1):
            return False

        import collections

        s1_map = collections.defaultdict(int)
        for c in s1:
            s1_map[c] += 1

        s1_chars = set(s1_map.keys())

        for idx in range(len(s2) - len(s1) + 1):
            if s2[idx] in s1_chars:
                s2_map = collections.defaultdict(int)
                for c in s2[idx:idx + len(s1)]:
                    s2_map[c] += 1

                if s1_map == s2_map:
                    return True

        return False

def check_inclusion_slide_window(s1, s2):
    class CharCounts(object):
        def __init__(self):
            self.counts = [0] * 26

        def all_zeros(self):
            for n in self.counts:
                if n != 0:
                    return False
            return True

        def upd_plus(self, char):
            self.counts[ord(char)-ord('a')] += 1

        def upd_minus(self, char):
            self.counts[ord(char)-ord('a')] -= 1

    counts = CharCounts()
    for idx in range(len(s1)):
        counts.upd_minus(s1[idx])
        counts.upd_plus(s2[idx])

    for idx in range(len(s1), len(s2)):
        if counts.all_zeros():
            return True
        counts.upd_plus(s2[idx])
        counts.upd_minus(s2[idx-len(s1)])

    if counts.all_zeros():
        return True

    return False

def main():
    s1 = "adc"
    s2 = "dcda"
    print(check_inclusion_slide_window(s1, s2))

if __name__ == '__main__':
    main()




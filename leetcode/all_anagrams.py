# https://leetcode.com/explore/featured/card/may-leetcoding-challenge/536/week-3-may-15th-may-21st/3332/

# Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.
#
# Strings consists of lowercase English letters only and
# the length of both strings s and p will not be larger than 20,100.
# The order of output does not matter.
#
# Example 1:
# Input:
# s: "cbaebabacd" p: "abc"
# Output:
# [0, 6]
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
#
# Example 2:
# Input:
# s: "abab" p: "ab"
# Output:
# [0, 1, 2]
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if not p or len(p) == 0:
            return []

        len_p = len(p)
        len_s = len(s)

        if not s or len_s < len_p:
            return []

        import collections
        # char counter for p:
        p_cnt = collections.defaultdict(int)
        for c in p:
            p_cnt[c] += 1
        p_cnt = dict(p_cnt)

        # initial char count for substring of s:
        s_cnt = collections.defaultdict(int)
        for c in s[:len_p]:
            s_cnt[c] += 1
        s_cnt = dict(s_cnt)

        result = []
        from_idx = 0
        last_idx = len_p - 1

        while True:
            if p_cnt == s_cnt:
                result.append(from_idx)

            from_idx += 1
            last_idx += 1
            if last_idx == len_s:
                break

            c_out = s[from_idx - 1]
            if s_cnt[c_out] > 1:
                s_cnt[c_out] -= 1
            else:
                del s_cnt[c_out]

            c_in = s[last_idx]
            if c_in in s_cnt:
                s_cnt[c_in] += 1
            else:
                s_cnt[c_in] = 1

        return result

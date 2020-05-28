# Given a string s and an integer k.
# Return the maximum number of vowel letters in any substring of s with length k.
#
# Vowel letters in English are (a, e, i, o, u).

# Example 1:
# Input: s = "abciiidef", k = 3
# Output: 3
# Explanation: The substring "iii" contains 3 vowel letters.

# Example 2:
# Input: s = "aeiou", k = 2
# Output: 2
# Explanation: Any substring of length 2 contains 2 vowels.

# Example 3:
# Input: s = "leetcode", k = 3
# Output: 2
# Explanation: "lee", "eet" and "ode" contain 2 vowels.

# Example 4:
# Input: s = "rhythms", k = 4
# Output: 0
# Explanation: We can see that s doesn't have any vowel letters.

# Example 5:
# Input: s = "tryhard", k = 4
# Output: 1
#

class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if not s or k <= 0:
            return 0

        vowels = {'a', 'o', 'e', 'i', 'u'}
        count = 0
        counts = [0]

        for c in s:
            if c in vowels:
                count += 1
            counts.append(count)

        maxv = 0
        for idx in range(len(s) - k + 1):
            maxv = max(maxv, counts[idx + k] - counts[idx])

        return maxv


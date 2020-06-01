# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/538/week-5-may-29th-may-31st/3346/

# Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

# You have the following 3 operations permitted on a word:
# Insert a character
# Delete a character
# Replace a character

# Example 1:
# Input: word1 = "horse", word2 = "ros"
# Output: 3
# Explanation:
# horse -> rorse (replace 'h' with 'r')
# rorse -> rose (remove 'r')
# rose -> ros (remove 'e')

# Example 2:
# Input: word1 = "intention", word2 = "execution"
# Output: 5
# Explanation:
# intention -> inention (remove 't')
# inention -> enention (replace 'i' with 'e')
# enention -> exention (replace 'n' with 'x')
# exention -> exection (replace 'n' with 'c')
# exection -> execution (insert 'u')

class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        dp = {}

        def get_distance(i, j):
            if (i, j) in dp:
                return dp[i, j]
            if i == len(word1):
                return len(word2) - j
            if j == len(word2):
                return len(word1) - i
            else:
                if word1[i] == word2[j]:
                    dp[i, j] = get_distance(i + 1, j + 1)
                else:
                    dp[i, j] = min(
                        get_distance(i + 1, j),
                        get_distance(i, j + 1),
                        get_distance(i + 1, j + 1)
                    ) + 1
                return dp[i, j]

        return get_distance(0, 0)

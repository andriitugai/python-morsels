# https://leetcode.com/problems/friends-of-appropriate-ages/

# Some people will make friend requests. The list of their ages is given and ages[i] is the age of the ith person.
#
# Person A will NOT friend request person B (B != A) if any of the following conditions are true:
#
# age[B] <= 0.5 * age[A] + 7
# age[B] > age[A]
# age[B] > 100 && age[A] < 100
# Otherwise, A will friend request B.
#
# Note that if A requests B, B does not necessarily request A.  Also, people will not friend request themselves.
#
# How many total friend requests are made?
#
# Example 1:
# Input: [16,16]
# Output: 2
# Explanation: 2 people friend request each other.

# Example 2:
# Input: [16,17,18]
# Output: 2
# Explanation: Friend requests are made 17 -> 16, 18 -> 17.

# Example 3:
# Input: [20,30,100,110,120]
# Output:
# Explanation: Friend requests are made 110 -> 100, 120 -> 110, 120 -> 100.

class Solution(object):
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """
        MAX_AGE = 120

        age_counts = [0] * (MAX_AGE + 1)
        for age in ages:
            age_counts[age] += 1

        total = 0
        for idx, age_count in enumerate(age_counts):
            if age_count:
                total += sum(age_counts[int(idx / 2 + 7) + 1: idx]) * age_count
                if idx > idx / 2 + 7:
                    total += age_count * (age_count - 1)

        return total



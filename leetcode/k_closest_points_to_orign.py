# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/538/week-5-may-29th-may-31st/3345/

# We have a list of points on the plane.  Find the K closest points to the origin (0, 0).
# (Here, the distance between two points on a plane is the Euclidean distance.)
# You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)
#
# Example 1:
# Input: points = [[1,3],[-2,2]], K = 1
# Output: [[-2,2]]
# Explanation:
# The distance between (1, 3) and the origin is sqrt(10).
# The distance between (-2, 2) and the origin is sqrt(8).
# Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
# We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].

# Example 2
# Input: points = [[3,3],[5,-1],[-2,4]], K = 2
# Output: [[3,3],[-2,4]]
# (The answer [[-2,4],[3,3]] would also be accepted.)

import random

class Solution(object):
    def dist(self, point):
        return point[0] ** 2 + point[1] ** 2

    def find_min_k(self, points_dists, K):
        if len(points_dists) == K:
            return [item[0] for item in points_dists]

        rnd_item = random.choice(points_dists)
        pivot = rnd_item[1]

        left = []
        equal = []
        right = []

        idx = 0
        while idx < len(points_dists):
            item = points_dists[idx]
            dist = item[1]

            if dist < pivot:
                left.append(item)
            elif dist == pivot:
                equal.append(item)
            else:
                right.append(item)

            idx += 1

        if len(left) == K:
            return [item[0] for item in left]
        if len(left) + len(equal) == K:
            return [item[0] for item in left] + [item[0] for item in equal]
        if len(left) > K:
            return self.find_min_k(left, K)
        else:
            return [item[0] for item in left] + self.find_min_k(equal + right, K - len(left))

    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        points_dists = [(point, self.dist(point)) for point in points]
        return self.find_min_k(points_dists, K)

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        # the simple insight here is that the minimum second is the
        # max of the values x or y between the two adjacent points.
        # We take the some accross all values to get the answer.

        n = len(points)
        ans = 0
        for i in range(1, n):
            x1, y1 = points[i-1]
            x2, y2 = points[i]

            ans += max(abs(x1- x2), abs(y2- y1))

        return ans



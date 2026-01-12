class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        # we can go with a greedy algorithm.
        # if the two points adjacent points (x or y axis)
        # are the same. the minimum second is the abs difference
        # of the x or y-axis (depending on the axis that's different)
        # other wise we'll choose to go diagonal 
        # (adding 1 second as we do so) until the x or y axis
        # are the same, and repeat the previous step.

        # e.g [
            # [3, 2], [-2, 5]
            # [3, 2], [5, 7]
        # ]

        n = len(points)
        ans = 0
        for i in range(1, n):
            x1, y1 = points[i-1]
            x2, y2 = points[i]

            ans += max(abs(x1- x2), abs(y2- y1))

        return ans



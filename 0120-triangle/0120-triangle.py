class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # let's try recursion with memoization.
        # Steps.
        # define base cases.
        # Do stuffs/ explore all paths.
        # take global optimum, in this case, min path.

        # the idea here is to assume, we
        # are going from bottom to top.
        # we can start from the 
        #1st, 2nd... or last number 
        # on the last row, and move up
        # until we get to the top (0,0)

        # we can only move:
        # - directly up 
        # - diagonally up left

        def f(i, j, dp):
            if i == 0 and j == 0:
                return triangle[0][0]
            if i < 0 or j < 0 or j >=len(triangle [i]):
                return float("inf")
            if dp[i][j] != None:
                return dp[i][j]

            #explore paths
            up = triangle[i][j] + f(i-1, j, dp)
            upl = triangle[i][j] + f(i-1, j-1, dp)

            dp[i][j] = min(up, upl)
            return dp[i][j]

        
        m = len(triangle)
        dp = [[None]*i for i in range(1, m+1)]
        ans = float("inf")
        for j in range(m):
            ans = min(ans, f(m-1, j, dp))
        return ans
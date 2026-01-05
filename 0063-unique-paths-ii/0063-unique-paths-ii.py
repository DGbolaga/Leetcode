class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        #steps:
        # - express everything in terms of index (i, j)
        # - explore all paths/ do stuffs
        # - take global optimum (sum/min/max) in this case, sum

        def f(i, j, grid, dp):
            #base cases
            if grid[i][j] == 1: return 0
            if i == 0 and j == 0: return 1
            if i < 0 or j < 0: return 0
            if dp[i][j] != -1: return dp[i][j]

            #explore paths
            up = f(i-1, j, grid, dp)
            left = f(i, j-1, grid, dp)
            
            dp[i][j] = up + left
            return dp[i][j]
        
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[-1 for _ in range(n)] for _ in range(m)]
        return f(m-1, n-1, obstacleGrid, dp)
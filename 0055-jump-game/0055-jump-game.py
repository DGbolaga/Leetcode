class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # express everything in terms of index (i, j)
        # do stuffs/ explore all paths.
        # find global optimum (can reach len(nums)-1)

        # memoization gave tle
        def f(i, dp):
            if i == len(nums)-1:
                return 1
            if i >= len(nums):
                return 0
            if dp[i] != -1:
                return dp[i]

            
            jumps = nums[i] 
            ans = float('-inf')
            for j in range(1, jumps+1):
                ans = max(ans, f(i+j, dp))

            dp[i] = ans
            return dp[i]
        
        # let's try tabulation
        def fT(nums):
            n = len(nums)
            dp = [0 for _ in range(n)]
            dp[n-1] = 1 #base case

            for i in range(n-2,-1,-1):
                for j in range(1, nums[i]+1):
                    if i + j < n and dp[i+j] == 1:
                        dp[i] = 1
                        break
                
            return dp[0]
                    
        res = fT(nums)
        return True if res == 1 else False

            
            
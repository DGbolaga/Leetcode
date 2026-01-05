class Solution:
    def rob(self, nums: List[int]) -> int:
        # explore all paths.
        def f(i, n, nums, dp):
            #base case
            if i >= n: return 0
            if dp[i] != -1: return dp[i]
            dp[i] = max(f(i+1, n, nums, dp), nums[i] + f(i+2, n, nums, dp))
            return dp[i]
        n = len(nums)
        dp = [-1 for _ in range(n)]
        return f(0, n, nums, dp)    
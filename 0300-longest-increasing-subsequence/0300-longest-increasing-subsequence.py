class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        def f(x, n, dp, prev):
            if x == n: return 0
            if dp[x][prev+1] != -1:
                return dp[x][prev+1]
            
            # not take
            not_take = f(x + 1, n, dp, prev) # pick ignore index, but take the previous index also.

            # take
            take = 0
            if prev == -1 or nums[prev] < nums[x]:
                take = 1 + f(x + 1, n, dp, x) # pick, move to next index and keep track of immediate previous index.


            dp[x][prev+1] = max(take, not_take)
            return dp[x][prev+1]

        n = len(nums)
        dp = [[-1 for _ in range(n+1)] for _ in range(n)]
        ans = f(0, n, dp, -1)

        return ans

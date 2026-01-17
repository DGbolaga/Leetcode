class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        # the idea here is to keep track
        # of the maximum length, by 
        # using an idea from the two sum
        # problem. If the current value
        # minus the target difference has
        # been seen, we would add 
        # the current value to a map,
        # and set its map val to 
        # current-diff + 1. In all this,
        # we'll keep track of the max
        # length as our answer.


        maxl = 1
        dp = {}
        for num in arr:
            target = num - difference 
            if target in dp:
                dp[num] = dp[target] + 1
                maxl = max(maxl, dp[num])

            else:
                dp[num] = 1
        return maxl
        
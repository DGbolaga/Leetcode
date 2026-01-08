from collections import defaultdict
class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        # the idea here is to define the possible moves we can make.
        # we can either take nums[i] * nums[j] with i and j signifying the index possible between len(nums1) and len(nuns2) respectively.
        # or we can take nums[i] only
        # or we can take nums[j] only
        # but at all cost we most take the maximum answer of all our options.
        # the bade case is simple, can't move futher if there is nothing to pick in either array i.e i or j is out of bound.
        
        def f(x, y, nums1, nums2, dp):
            if x >= len(nums1) or y >= len(nums2):
                return float("-inf")
            if dp[x][y] != None:
                return dp[x][y]

            ans = float("-inf")

            ans = max(ans, nums1[x] * nums2[y] + max(0, f(x+1, y+1, nums1, nums2,dp))) # it's important that the sub options return 0 and not -inf because -inf will reduce the previous result to -inf.
            ans = max(ans, f(x, y+1, nums1, nums2, dp))
            ans = max(ans, f(x+1, y, nums1, nums2, dp))

            dp[x][y] = ans
            
            return dp[x][y]
        n1 = len(nums1)
        n2 = len(nums2)
        dp = [[None] * (n2) for _ in range(n1)]
        
        return f(0,0,nums1,nums2,dp)
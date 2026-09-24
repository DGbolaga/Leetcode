class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n//2
        cnt = 0
        while r < n and l < n//2:
            if nums[r] != nums[l]:
                cnt += 2
                l += 1
                r += 1
            
            else:
                r += 1
        
        return n - cnt
        
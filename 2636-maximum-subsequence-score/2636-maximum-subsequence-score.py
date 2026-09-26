class Solution:
    def maxScore(self, nums1: list[int], nums2: list[int], k: int) -> int:
        # brute force way is to find all substring in nums1 of length k, and get in constant time the minimum from nums2.
        # the maximum function is our response.
        # to kind all subsequence in nums1 is O(n**2) = 10**10 not possilbe by brute force.
        # so we need an optimum strategy.
        # to maximize the our function of f(x) where x is the sum of values in subsequence x.. such that it's gives the maximum when multiplied by the minimum in the subsequence of values in nums2.

        # we can assume that it will take the same time to check nums1 for subsequence of k, the same time it will take check nums2 for the minimum (relatively constant time as we build nums1 subsequence)
        # n = len(nums1)
        # def rec(i, pick):
        #     if len(pick) == k:
        #         total, m = 0, float('inf')
        #         for i in pick:
        #             total += nums1[i]
        #             m = min(m, nums2[i])
        #         return total * m
        #     if i == n:
        #         return 0

        #     ans = float('-inf')
                
        #     if len(pick) < k:
        #         pick.append(i)
        #         ans = max(ans, rec(i+1, pick))
        #         pick.pop()
            
        #     ans = max(ans, rec(i+1, pick))

        #     return ans

        # return rec(0, [])
        # total = sum(nums1)
        # new = sorted(zip(nums1, nums2), key=lambda x: total * x[1])
        # # new = sorted(list(zip(nums1, nums2)), key=lambda x: nums1[x[0]] * nums2[x[1]])

        # # print(new)
        # # return 0
        # ans = 0
        # minV = float('inf')
        # for _ in range(k):
        #     a, b = new.pop()
        #     ans += a
        #     minV = min(minV, b)

        # return ans * minV

        # the idea here is to have it in sorted from reverse.
        # the strategy is to keep get the maximum function value.
        # [1,3,3,2] = [2,3,1,3]
        # [2,1,3,4] = [4,3,2,1]
        
        # then we start picking via a minheap to ensure that we pick the minimum so far of nums2

        arr = sorted(zip(nums1, nums2), key=lambda x: x[1], reverse=True)

        minHeap = []
        ans = 0
        total = 0
        for x, y in arr: # y  is in decreasing order
            heapq.heappush(minHeap, x)
            total += x

            if len(minHeap) > k:
                total -= heapq.heappop(minHeap)
            
            if len(minHeap) == k:
                ans = max(ans, total * y) # as why is garaunteed to be the minimum so far.

        
        return ans



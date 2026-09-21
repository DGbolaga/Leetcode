class Solution:
    def deleteAndEarn(self, nums: list[int]) -> int:
        # to maximize gains
        # max to gain point, by deleting, then set every element at val-1, val+1, to deleted.

        # this is just dp.

        # we need a sum of total, and one of unavailable.

        # I miss read the problem

        # what we need to do is to maintain a map, and perfrom ususal dp.

        mp = Counter(nums)
        arr = sorted(list(set(nums)))
        cache = {}
        n = len(arr)

        def rec(i):
            if i >= n:
                return 0

            if i in cache:
                return cache[i]

            ans = float("-inf")
            # skip
            ans = max(ans, rec(i+1))

            # take
            take = 0
            if i+1 < n and arr[i+1] - arr[i] > 1:
                take = arr[i]*mp[arr[i]] + rec(i+1)
            else:
                take = arr[i] * mp[arr[i]] + rec(i+2)

            ans = max(ans, take)
            cache[i] = ans

            return cache[i]
        
        ans = rec(0)
        return ans
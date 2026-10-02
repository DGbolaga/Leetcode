class Solution:
    def countTriplets(self, arr: list[int]) -> int:
        # let's brute force this.
        #
        ans = 0
        n = len(arr)
        for i in range(n):
            a = arr[i]
            for j in range(i+1, n):
                a ^= arr[j]
                b  = arr[j]
                for k in range(j, n):
                    b ^= arr[k]
                    if i < j <= k and a == b:
                        ans += 1

        return ans

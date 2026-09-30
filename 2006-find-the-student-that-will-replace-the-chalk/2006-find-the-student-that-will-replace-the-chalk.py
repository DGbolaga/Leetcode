class Solution:
    def chalkReplacer(self, chalk: list[int], k: int) -> int:
        #    3  4  1  2
        #25 -22 18 17 15
        #15 -12 8  7  5
        #5  -2  

        # this is typically math + hashing.
        # cause we can't brute force this.
        n = len(chalk)
        
        # why did I take so long to solve this.
        temp = k
        start = -1
        total = 0
        for i, val in enumerate(chalk):
            if total + val <= k:
                total += val
            else:
                start = i
                break
        
        if total >= k:
            return start if start != -1 else 0
        else:
            new_k = k % sum(chalk)
            for i, val in enumerate(chalk):
                if new_k - val >= 0:
                    new_k -= val
                else:
                    return i


        
      
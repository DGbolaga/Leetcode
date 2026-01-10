class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        # we can express everything in terms of i and j. i reps possible index in len(s1) and j in len(s2)

        # we want to track values that are not the same.
        # Inorder words we want to find the minimum sum of words that must be removed to make s1 and s2 the same.

        def f(x, y, dp):
            #base cases
            if x < 0:
                # the remaining of s2 can only be the answer.
                return sum(ord(s2[j]) for j in range(y+1))
            if y < 0:
                return sum(ord(s1[j]) for j in range(x+1))

            if dp[x][y] != -1:
                return dp[x][y]

            # explore all paths.
            ans = 0
            m1 = 0 # don't pick if they are the same.
            if s1[x] != s2[y]:
                m1 += ord(s1[x]) + ord(s2[y])
            m1 += f(x-1, y-1, dp) # move together 
            
            m2 = ord(s1[x]) + f(x-1, y, dp)
            m3 = ord(s2[y]) + f(x, y-1, dp)
            
            ans = min(m1, m2, m3)
                
            dp[x][y] = ans
            return dp[x][y]

        n, m = len(s1), len(s2)
        dp = [[-1] * (m) for _ in range(n)]
        return f(n-1, m-1, dp)
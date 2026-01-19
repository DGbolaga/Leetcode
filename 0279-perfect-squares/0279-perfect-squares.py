class Solution:
    def numSquares(self, n: int) -> int:
        # look for perfect squares less than n.
        sqrs = []
        for i in range(1, int(n**0.5)+1):
            sqrs.append(i**2)

        # we now have an unbounded knapsack problem.
        # where we want to know the least number of values
        # that can sum to n given that there are infinite
        # number of each value.
        
        # memoization. I got time limit exceeded.
        def f(i, total, sack_len, dp):
            #base cases.
            if total == n:
                return sack_len
            if total > n or i == len(sqrs):
                return float("inf")
            if dp[i][total][sack_len] != -1:
                return dp[i][total][sack_len]

            #explore all cases.
            pick = f(i, total+sqrs[i], sack_len+1, dp)
            npick = f(i+1, total, sack_len, dp)

            dp[i][total][sack_len] = min(pick, npick)
            return dp[i][total][sack_len]

        # dp = [[[-1] * (n+1) for i in range(n+1)] for j in range(n+1)] #it's easier to use a dict here.
        # return f(0, 0, 0, dp)


        # Let's try out the tabulation (bottom-up) approach.
        # on second thoughts, I'm modelling the problem wrongly.
        # The previous approach will always give me a O(sqrt(n) * n * n) solution which will 
        # never pass as it's too large.

        # we can rephrase the question as what's the least number of perfect squares we can 
        # substract from n to make it zero.

        def leastNumber(num, dp):
            if num == 0:
                return 0
            if dp[num] != -1:
                return dp[num]

            ans = float('inf')
            for x in sqrs:
                if x > num:
                    break
                ans = min(ans, 1+leastNumber(num - x, dp))
            
            dp[num] = ans
            return dp[num]
        dp = [-1] * (n+1)
        return leastNumber(n, dp)


        

        

            

        
        
class Solution:
    def numOfWays(self, n: int) -> int:
        # get the number of options per row, which is 12 from the test case. 
        # we can use that as our options in a recursive solution. for every option 
        # we select, the next row (values) must not be the same, so we'll have to pass our 
        # options on the next row during the recursive step.
        options = [
            "012",
            "010",
            "021",
            "020",
            "102",
            "101",
            "120",
            "121",
            "201",
            "202",
            "210",
            "212",
        ]
        # recursive - exponential TC
        def fR(i, p0, p1, p2, n, options):
            # base case.
            if i == n:
                return 1

            # explore all case.
            ans = 0
            for opt in options:
                c0, c1, c2 = int(opt[0]), int(opt[1]), int(opt[2])
                if c0 != p0 and c1 != p1 and c2 != p2:
                    ans += fR(i + 1, c0, c1, c2, n, options)

            return ans
        # return f(0, -1, -1, -1, n, options)

        # since our recursive solution gave tle, we can use memoization on it
        # memoization - linear TC (N * 12) where 12 represnets the number of options.
        # the recursive solution is based on 4 changing variables hence we'll declare a 4D dp array.
        dp = [
            [[[-1 for _ in range(3)] for _ in range(3)] for _ in range(3)]
            for _ in range(n)
        ]
        def fM(i, p0, p1, p2, n, options, dp):
            # base cases
            if i == n: return 1
            if dp[i][p0][p1][p2] != -1: return dp[i][p0][p1][p2]

            # explore all case.
            ans = 0
            for opt in options:
                c0, c1, c2 = int(opt[0]), int(opt[1]), int(opt[2])
                if c0 != p0 and c1 != p1 and c2 != p2:
                    ans += fM(i + 1, c0, c1, c2, n, options, dp)
            dp[i][p0][p1][p2] = ans % (10**9 + 7)
            return dp[i][p0][p1][p2]

        return fM(0, -1, -1, -1, n, options, dp)



            
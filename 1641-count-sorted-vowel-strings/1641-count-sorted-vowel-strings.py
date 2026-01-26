class Solution:
    def countVowelStrings(self, n: int) -> int:
        # the idea here is we are creating a subsequence
        # from the vowels in the english alphabet, which are
        # sorted, recursion and memoization will work best here.
        
        def f(count, curr):
            #base case.
            if count == n:
                return 1
            if (count, curr) in dp:
                return dp[(count, curr)]

            ans = 0
            for next in range(5):
                if curr <= next:
                    ans += f(count+1, next)
            
            dp[(count, curr)] = ans
            return dp[(count, curr)]

        dp = {}
        return f(0, 0)
        
            
            
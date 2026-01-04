class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        # we only need to count from 1 till the sqrt of a number to know it's
        # divisors. With this we can determine the numbers whose divisors
        # are exactly equals to 4.
        ans = 0
        for num in nums:
            res = 0
            count = 0
            sqrt = int(num**0.5)
            for i in range(1, sqrt+1):
                if num % i == 0:
                    divisor = num // i
                    res = res + i + divisor if divisor != sqrt else res + i
                    count = count + 2 if divisor != sqrt else count + 1
            if count == 4:
                ans += res
        return ans
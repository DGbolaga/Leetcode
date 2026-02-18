class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for _ in range(32):
            last_bit = n & 1
            n >>= 1
            ans <<= 1
            ans |= last_bit
        
        return ans

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        # we can xor every alternating bit i.e from 1 to n (x-1, x)
        # if we get a 0 then it doesn't alternate, else it's valid.

        prev_bit = n & 1 # last bit
        n >>= 1
        while n > 0:
            next_bit = n & 1
            if not (prev_bit ^ next_bit):
                return False
            
            n >>= 1
            prev_bit = next_bit
        
        return True
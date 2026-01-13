class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        # the brute force approach to this is simple.
        
        ans = 0
        t = word
        while t in sequence:
            ans += 1
            t += word
        return ans
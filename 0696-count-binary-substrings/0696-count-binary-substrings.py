class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        freq = []
        prev = s[0]
        n = len(s)
        count = 1
        for i in range(1, n):
            if s[i] == prev:
                count += 1
            else:
                freq.append(count)
                count = 1
                prev = s[i]
        freq.append(count)
        
        res = 0
        len_f = len(freq)
        for j in range(1, len_f):
            res += min(freq[j], freq[j-1])

        return res

            
            
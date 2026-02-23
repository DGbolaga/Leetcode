class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        # 1 val = 0, 1
        # 2 val = 00 10 01 11
        # 3 val = 000 001 010
        # 0 0 0 = 000, 001 010, 011, 100oi
        # 0 0 1
        # 0 1 0
        # 0 1 1
        # 1 0 0
        # 1 0 1
        # 1 1 0
        # 1 1 1

        seen = set()
        len_s = len(s)
        for i in range(len_s - k+1):
            if len(seen) == 2**k:
                break

            temp = int(s[i:i+k], 2)
            if temp not in seen:
                seen.add(temp)

        print(seen)
        for j in range(2**k):
            if j not in seen:
                return False
        
        return True
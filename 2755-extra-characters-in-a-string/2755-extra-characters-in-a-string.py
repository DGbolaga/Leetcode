class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        # get overlaps.
        def find(word, sub):
            n = len(word)
            m = len(sub)
            arr = []
            for i in range(n-m+1):
                if word[i:i+m] == sub:
                    arr.append(i)
            
            return arr

        pair = []
        for val in dictionary:
            
            res = find(s, val)
            if res != []:
                for i in res:
                    pair.append((i, i+len(val)-1))

        
        # now the max pick
        pair.sort()
        n = len(pair)
        memo = {}

        def rec(i, prev):
            #base case
            if i == n:
                # do something
                return 0
            key = (i, prev)
            if key in memo:
                return memo[key]

            # explore all case
            ans = float('-inf')
            if prev < pair[i][0]:
                #take
                ans = max(ans, pair[i][1]-pair[i][0]+1 + rec(i+1, pair[i][1]))

            ans = max(ans, rec(i+1, prev)) # skip

            memo[key] = ans
            return memo[key]

        return len(s) - rec(0, -1)
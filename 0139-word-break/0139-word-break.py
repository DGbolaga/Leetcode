class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # My solution to the word break problem on Leetcode (139).
        # The idea here is to seperate the wordDict into dict of arrays
        # where the key is the first letter in a word, and the value 
        # is an array contain all the wwords that begin with such 
        # letter.
        # At every index, we check if we can extend the sequence by a 
        # a value in map, if not we'll backtrack, and check another word
        # in that array.
        def f(i, pick):
            if i >= len(s):
                if pick == s:
                    dp[(i, pick)] = True
                    return dp[(i, pick)] 
                dp[(i, pick)] = False #else
                return dp[(i, pick)] 

            if (i, pick) in dp:
                return dp[(i, pick)] 
            
            # check if we have a valid sequence or the next starting
            # sequence is possible.
            if s[:len(pick)] != pick or s[i] not in mp:
                return False
                
            # check all options 
            ans = False
            for word in mp[s[i]]:
                ans = ans or f(i+len(word), pick+word)

            dp[(i, pick)] = ans
            return dp[(i, pick)] 

        mp = {}
        for word in wordDict:
            if word[0] not in mp:
                mp[word[0]] = [word]
            else:
                mp[word[0]].append(word)
        dp = {}
        return f(0, '')
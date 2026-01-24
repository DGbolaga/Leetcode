class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        
        ans = []
        prev = -1
        for i in range(len(groups)):
            if prev == -1 or groups[i] != prev:
                prev = groups[i]
                ans.append(words[i])

        return ans

        
            





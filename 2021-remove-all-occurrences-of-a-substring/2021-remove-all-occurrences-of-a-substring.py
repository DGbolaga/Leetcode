class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        # let's use bruteforce as usual, then we can optimize.

        stack = []
        n = len(part)
        part = list(part)

        for ch in s: # 1000 at most.
            stack.append(ch)
            while stack and stack[-n:] == part: # 1000 at most
                # for _ in range(n):
                #     stack.pop()
                m = len(stack)
                stack = stack[:m-n] # this is at 1000 to 0 depending on len(stack), cause if n is at most 1000 the difference is little.. it should still pass.
        
        return "".join(stack)
            
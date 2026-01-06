class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        # this is a very very tricky question.
        # the idea again is understand the requirement and describe the base case.
        # steps:
        # - express everything in terms of index (i, j)
        # - explore all paths /Do stuffs
        # - take global optimum (min number of jumps)

        # tried using dp, but didn't work. let's use bfs. By trial and error,
        # if we jump to a position highest(max(forbidden_value), x) + a + b,
        # no matter what we do, we won't enter back into the correct window i.e 0 to X (inclusive). so we can set a max_limit as that.
        bfs = [(0, 0)] # position, and back_used (0 or 1)
        count, seen = 0, set([0, 0])
        forbidden = set(forbidden)
        max_limit = max(max(forbidden), x) + a + b
        while bfs:
            newbfs = []
            for num, back_used in bfs:
                if num == x:return count
                # move forward if within max_limit, value hasn't been seen 
                # and, is not among the forbidden spots.
                forward = num + a
                value = (forward, 0)
                if (forward not in forbidden and forward <= max_limit and value not in seen):
                    seen.add(value)
                    newbfs.append(value)

                # we can only jump backward 
                # if we haven't jumped backward previously.
                # we can only jump to a backward position that's not in forbidden
                # i.e (any position < 0 is forbidden) and value hasn't been seen.
                if back_used == 0:
                    backward = num - b
                    value = (backward, 1)
                    if (backward not in forbidden and backward >= 0 
                        and value not in seen):
                        seen.add(value)
                        newbfs.append(value)
            bfs = newbfs
            count += 1
        return -1
           
        
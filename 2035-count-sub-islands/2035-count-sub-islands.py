class Solution:
    def countSubIslands(self, grid1: list[list[int]], grid2: list[list[int]]) -> int:
        # my approach to this is simple
        # get all the island in grid2 and grid1
        # check all the island in grid2 that are a subset of grid1

        # bruteforce.
        # m, n = len(grid1), len(grid1[0])
        # ones1 = set()
        # ones2 = set()

        # for i in range(m):
        #     for j in range(n):
        #         if grid1[i][j] == 1:
        #             ones1.add((i, j))
        #         if grid2[i][j] == 1:
        #             ones2.add((i, j))

        # island2 = []
        # def makeIsland(arr):
        #     islands = []
        #     while arr:
        #         head = arr.pop()
        #         bfs = {head}
        #         island = {head}
        #         while bfs:
        #             newbfs = set()
        #             for i,j in bfs: # node
        #                 for x, y in [(0,1), (0,-1), (1,0), (-1, 0)]:
        #                     if (0<=i+x<m and 0<=j+y<n) and (i+x, j+y) in arr:
        #                             newbfs.add((i+x, j+y))
        #                             arr.discard((i+x, j+y))
        #                             island.add((i+x, j+y))
        #             bfs = newbfs

        #         islands.append(island)

        #     return islands
        
        # island1 = makeIsland(ones1)
        # island2 = makeIsland(ones2)

        # ans = 0
        # for block2 in island2:
        #     for block1 in island1:
        #         if block2.issubset(block1):
        #             ans += 1


        # return ans

        # a better way.
        # as we find the islands in grid2, we just check the ones that are already in grid1.
        m, n = len(grid1), len(grid1[0])
        arr = set((i, j) for i, j in product(range(m), range(n)) if grid2[i][j] == 1) # grid2

        res = 0
        islands = []
        while arr:
            head = arr.pop()
            bfs = {head}
            island = {head}
            ans = True if grid1[head[0]][head[1]] == 1 else False
            while bfs:
                newbfs = set()
                for i,j in bfs: # node
                    for x, y in [(0,1), (0,-1), (1,0), (-1, 0)]:
                        if (0<=i+x<m and 0<=j+y<n) and (i+x, j+y) in arr:
                                newbfs.add((i+x, j+y))
                                arr.discard((i+x, j+y))
                                island.add((i+x, j+y))

                                if grid1[i+x][j+y] == 0:
                                    ans = False
                bfs = newbfs

            if ans == True:
                res += 1
            islands.append(island)

        return res

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: TreeNode | None, start: int) -> int:
        # the best thing to do is to convert this to a graph and perfrom bfs on it.

        self.G = defaultdict(set)
       
        def rec(node, parent):
            if node == None:
                return 

            if parent:
                self.G[parent.val].add(node.val)
                self.G[node.val].add(parent.val)

            rec(node.left, node)
            rec(node.right, node)

        rec(root, None)

        # now we can perfrom bfs.
        bfs = {start}
        seen = set()
        lvl = -1
        while bfs:
            newbfs = set()
            for node in bfs:
                seen.add(node)
                for nei in self.G[node]:
                    if nei not in seen:
                        newbfs.add(nei)
                
            lvl +=1 
            bfs = newbfs
        
        return lvl
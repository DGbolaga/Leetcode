# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        # perform bfs on this.
        if not root:
            return []
            
        ans = []
        bfs = [root]
        while bfs:
            newbfs = []
            for node in bfs:
                if node.left:
                    newbfs.append(node.left)
                if node.right:
                    newbfs.append(node.right)
            ans.append(bfs[-1].val)
            bfs = newbfs 
        
        return ans

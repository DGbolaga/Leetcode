# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        ans = float("-inf")
        bfs = [root]
        level = 0
        count = 1
        while bfs:
            newbfs = []
            sumV = 0
            for node in bfs:
                sumV += node.val
                if node.left:
                    newbfs.append(node.left)
                if node.right:
                    newbfs.append(node.right)
            
            if sumV > ans:
                level = count
                ans = sumV
            
            bfs = newbfs
            count += 1
        return level
                
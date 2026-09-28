# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: TreeNode | None) -> bool:
        # just simple bfs.

        bfs = [root]
        lvl = 0
        while bfs:
            newbfs = []
            prev = None

            for i, node in enumerate(bfs):
                if lvl % 2 == 0: # even level
                    if (prev and prev >= node.val) or node.val % 2 == 0:
                        return False
                else:
                    if (prev and prev <= node.val) or node.val % 2 == 1:
                        return False
                prev = node.val

                if node.left:
                    newbfs.append(node.left)
                if node.right:
                    newbfs.append(node.right)

                

            lvl +=1
            bfs = newbfs

        return True
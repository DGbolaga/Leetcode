# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
        if root == None:
            root = TreeNode(val=val)
            return root

        def insert(node):
            if node == None:
                return 

            if node.val > val:
                if node.left:
                    insert(node.left)
                else:
                    node.left = TreeNode(val=val)
            
            if node.val < val:
                if node.right:
                    insert(node.right)
                else:
                    node.right = TreeNode(val=val)

        insert(root)
        return root
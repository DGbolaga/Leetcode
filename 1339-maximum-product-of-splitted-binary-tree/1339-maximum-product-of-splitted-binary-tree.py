# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        
        #with the hints giving,
        # we need to traverse every node
        # and get the max product based 
        # on the formula: 
        # return max((total_sum - sub_tree) * sub_tree), where sub tree refers to the total sum in a sub tree.

        #we can use preorder tree traversal to get the sum
        ans = [0]

        def pre(node, ans):
            if node is None:
                return 
            ans[0] += node.val
            pre(node.left, ans)
            pre(node.right, ans)

        pre(root, ans)

        res = [-1]
        # a post order traversal is suiteable for this problem
        def inorder(node,res, total):
            if node is None:
                return 0

            l = inorder(node.left, res ,total)
            r = inorder(node.right, res, total) 
            subtree_sum = node.val + l + r
            res[0] = max(res[0], (total-subtree_sum) * subtree_sum)
            return subtree_sum
            

        inorder(root, res, ans[0])
        return res[0] % (10**9 + 7)
        

            
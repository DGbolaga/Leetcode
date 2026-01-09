# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # what is a deepnode? a node that is farthest away from the 
        # root node.
        # Is it safe to say that the smallest sub tree can only 
        # consist of 3 nodes? Yes, its safe to say so.
        # In the example 5 is not referred to as the smallest subtree
        # all though it has a child that is also deep but not the 
        # depeest. On the other hand 2 is referred to as the smallest
        # subtree because but it's children are the depeest node.
        # however if one of the children of 2 where missing i.e
        # the node 2 has only one child, 2 will not be the smallest
        # subtree because it has a descendant. If 2 had no child, 
        # it becomes a leaf node as such it can't be the smallest 
        # subtree, because it has a parent.

        # From this, we can say that the parent of the node that is
        # the deepest is what we are looking for.

        # if only one node, that's our answer.
        if root.left is None and root.right is None: return root


        # Since all the nodes are unique, we can keep track of the 
        # children as key and parent as index, so we can easily 
        # retrieve the answer.

        # a bfs is best used here to know the deepest node.
        # after going down this path, my found my analysis was wrong.
        
        # a better approach will be to find the deepest leaf node
        # using bfs.
        # If there is only 1 deep node, we've found our answer.
        # if there are multiple deep nodes, we'll trace them back
        # through their parents until they reach the same parent, 
        # which will be the node we are looking for.
        # to trace them back, we'll keep a map (child as key and 
        # parent as value)

        bfs = [root]
        mp = {}
        deepestNode = []
        while bfs:
            newbfs = []
            for node in bfs:
                if node.left:
                    newbfs.append(node.left)
                    mp[node.left.val] = node
                if node.right:
                    newbfs.append(node.right)
                    mp[node.right.val] = node
            if not newbfs:
                # empty
                deepestNode = bfs
            bfs = newbfs
        
        if len(deepestNode) == 1:
            return deepestNode[0]

        # keep moving up in each deepNode until a unified parent is 
        # meet.
        ans = set(deepestNode)
        while len(ans) != 1:
            newAns = set()
            for node in ans:
                newAns.add(mp[node.val])
            ans = newAns
        

        return ans.pop()
                


                
                

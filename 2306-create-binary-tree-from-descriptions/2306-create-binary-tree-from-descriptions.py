# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: list[list[int]]) -> TreeNode | None:
        # let's assemble this as a graph

        G = defaultdict(lambda : [0, 0])
        children = set()
        parent = set()
        for opt in descriptions:
            node, child, isleft = opt
            if isleft:
                G[node][0] = child
                children.add(child)
            else:
                G[node][1] = child
                children.add(child)

            parent.add(node)

        root = None
        for node in parent:
            if node not in children:
                root = node
                break
        
        def build(node):
            #base case.
            if node not in G:
                return TreeNode(node)

            newNode = TreeNode(node)
            l, r = G[node]
            if l:
                newNode.left = build(l)
            if r:
                newNode.right = build(r)
            
            G.pop(node)

            return newNode
        
        return build(root)
                


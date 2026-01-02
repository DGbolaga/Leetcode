"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # create a direct copy of the list using map.
        # connect the nodes in the map.values all together.
        # i.e with the key (original node) points to in the map.keys
        # and the value pair, should also point to it's equivalent in the
        # map.values.
        if not head: return None
        
        mp = {}
        curr = head
        while curr:
            mp[curr] = Node(curr.val)
            curr = curr.next
        

        curr = head
        while curr:
            temp = mp[curr]
            temp.next = mp[curr.next] if curr.next else None
            temp.random = mp[curr.random] if curr.random else None

            curr = curr.next

        return mp[head]
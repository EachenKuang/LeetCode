"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution1:
    def connect(self, root: 'Node') -> 'Node':
        temp = root
        while root and root.left:
            next = root.left
            while root:
                root.left.next = root.right
                if root.next:
                    root.right.next = root.next.left
                else:
                    root.right.next = None
                root = root.next
            root = next
        return temp

class Solution2:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        
        queue = [root]
        while queue:
            for i in range(len(queue)-1):
                queue[i].next = queue[i+1]
            queue[-1].next = None
            tmp = []
            for node in queue:
                tmp.extend([node.left, node.right])
            
            queue = [n for n in tmp if n]
        return root
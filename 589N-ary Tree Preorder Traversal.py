"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        result = []
        if root is None:
            return []
        for i in root.children:
            if i.children is None:
                result.append(i.val)
            else:
                result.extend(self.postorder(i))
        result.append(root.val)
        return result

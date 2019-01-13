"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if root is None:
            return 0
        else:
            children = root.children
            if len(children) == 0:
                return 1
            else:
                max = 0
                for i in children:
                    tmp = self.maxDepth(i)
                    if tmp>max:
                        max = tmp
                return max+1




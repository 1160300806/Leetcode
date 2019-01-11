
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        q=[]
        result = 0
        q.append(root)
        while len(q)!=0:
            tmp=q.pop(0)
            if tmp.val > L and tmp.val < R:
                if tmp.left != None:
                    q.append(tmp.left)
                if tmp.right != None:
                    q.append(tmp.right)
                result += tmp.val
            elif tmp.val < L:
                if tmp.right != None:
                    q.append(tmp.right)
            elif tmp.val > R:
                if tmp.left != None:
                    q.append(tmp.left)
            elif tmp.val == L:
                if tmp.right != None:
                    q.append(tmp.right)
                result += tmp.val
            elif tmp.val == R:
                if tmp.left != None:
                    q.append(tmp.left)
                result += tmp.val
        return result

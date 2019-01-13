# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def allPossibleFBT(self, N):
        """
        :type N: int
        :rtype: List[TreeNode]
        """
        if N % 2 == 0:
            return []
        else:
            if N == 1:
                root = TreeNode(0)
                return [root]
            else:
                result=[]
                for i in range(1,N-1,2):
                    tmp1=self.allPossibleFBT(i)
                    tmp2=self.allPossibleFBT(N-1-i)

                    for j in tmp1:
                        for k in tmp2:
                            root = TreeNode(0)
                            root.left = j
                            root.right = k
                            result.append(root)

                return result



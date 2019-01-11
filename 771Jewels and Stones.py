class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        cnt=0
        for i in range(len(J)):
            cnt += S.count(J[i])
        return cnt

class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        cnt = 1
        result = 0
        for i in range(len(s)-1,-1,-1):
            result += cnt*(ord(s[i])-64)
            cnt *= 26
        return result



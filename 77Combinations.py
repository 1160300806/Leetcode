class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if n < k:
            return []
        else:
            if k == 1:
                result = []
                for i in range(n):
                    tmp = []
                    tmp.append(i)
                    result.append(tmp)
                return result
            else:
                result = []
                result1 = self.combine(n-1,k-1)
                result2 = self.combine(n-1,k)
                for i in result1:
                    i.append(n)
                    result.append(i)
                result.extend(result2)
                return result



class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row_maxes = [max(row) for row in grid]
        col_maxes = [max(col) for col in zip(*grid)]

        res = 0
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                res += min(row_maxes[r], col_maxes[c]) - val
        return res


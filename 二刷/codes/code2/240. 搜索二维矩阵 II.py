from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        m, n = len(matrix), len(matrix[0])

        def dfs(i, j, target):
            if not (0 <= i < m and 0 <= j < n):
                return False

            if matrix[i][j] == target:
                return True

            if matrix[i][j] > target:
                return dfs(i, j - 1, target)
            else:
                return dfs(i + 1, j, target)

        return dfs(0, n - 1, target)
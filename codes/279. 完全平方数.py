import math
import math


class Solution:
    def numSquares(self, n: int) -> int:

        df = [int(math.inf)] * (n + 1)
        df[0] = 0

        for i in range(1, n + 1):
            for j in range(1, int(math.sqrt(i)) + 1):
                df[i] = min(df[i], df[i - j * j] + 1)

        return df[n]

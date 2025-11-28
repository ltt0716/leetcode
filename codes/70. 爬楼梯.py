class Solution:
    def climbStairs(self, n: int) -> int:
        ans = 0
        cnt = {0: 1, 1: 1}

        for i in range(2, n + 1):
            cnt[i] = cnt[i - 1] + cnt[i - 2]

        ans = cnt[n]

        return ans
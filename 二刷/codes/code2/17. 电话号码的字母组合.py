from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        cnt = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "nmo",
            7: "pqrs",
            8: "tuv",
            9: "wxyz"
        }
        ans = []
        cur = ""
        n = len(digits)

        def backtracking(i):
            nonlocal cur, n
            if i == n:
                ans.append(cur[:])
                return

            for c in cnt[int(digits[i])]:
                cur += c
                backtracking(i + 1)
                cur = cur[0:-1]

        backtracking(0)
        return ans

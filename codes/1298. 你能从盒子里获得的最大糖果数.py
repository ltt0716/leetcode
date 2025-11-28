import collections
from typing import List


class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]],initialBoxes: List[int]) -> int:
        n=len(status)

        ans=0

        q=collections.deque()

        nokeybox=set()

        havekeys=set()



        for i in initialBoxes:
            if status[i]==1:
                q.append(i)
            else:
                nokeybox.add(i)

        # print(len(nokeybox),havekeys,q)
        while q:
            cur=q.popleft()

            ans+=candies[cur]

            if keys[cur]:
                # print(keys[cur])
                havekeys.update(set(keys[cur]))
                # print(havekeys)

            # print(cur,ans)

            for i in containedBoxes[cur]:
                if status[i]==1:
                    q.append(i)
                else:
                    nokeybox.add(i)

            for i in nokeybox.copy():
                if i in havekeys.copy():
                    q.append(i)
                    havekeys.remove(i)
                    nokeybox.remove(i)

        return ans


status = [1,0,1,0]
candies = [7,5,4,100]
keys = [[],[],[1],[]]
containedBoxes = [[1,2],[3],[],[]]
initialBoxes = [0]

print(Solution().maxCandies(status, candies, keys, containedBoxes, initialBoxes))
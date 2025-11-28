import collections
from collections import defaultdict
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        g = defaultdict(list)
        pri=defaultdict(list)

        for u,v in prerequisites:
            g[v].append(u)
            pri[u].append(v)


        pri1 = pri.copy()
        visited = set()
        course=[]
        q = collections.deque()


        for i in range(numCourses):
            if len(pri1[i])!=0:
                continue
            visited.add(i)
            course.append(i)
            q.append(i)

        while q:
            cur = q.popleft()

            for v in g[cur]:
                if cur in pri[v]:
                    pri[v].remove(cur)

                if v not in visited:
                    if pri[v] == []:
                        q.append(v)
                        visited.add(v)
                        course.append(v)

        if len(course) == numCourses:
            return course

        return []
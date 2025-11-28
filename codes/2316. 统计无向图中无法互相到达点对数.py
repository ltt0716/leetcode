from typing import List


class Graph:
    def __init__(self, n):
        self.n = n
        self.adj = [[] for _ in range(n)]


class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:

        G = Graph(n)
        visited = [False] * n
        paths = []
        path = []
        ans = 0

        for neigbor in edges:
            v1, v2 = neigbor[0], neigbor[1]
            G.adj[v1].append(v2)
            G.adj[v2].append(v1)

        def dfs(i: int):
            # nonlocal path,paths
            if visited[i] == True:
                return
            path.append(i)
            visited[i] = True

            for edge in G.adj[i]:
                if not visited[edge]:
                    dfs(edge)

        for i in range(n):
            path = []
            dfs(i)
            if path:
                paths.append(path.copy())
                ans += len(path) * (n - len(path))

        # print(paths)

        return int(ans / 2)


n = 5
edges = [[1, 0], [3, 1], [0, 4], [2, 1]]
print(Solution().countPairs(n, edges))

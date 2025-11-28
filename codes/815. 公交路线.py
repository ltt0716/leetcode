import collections
from typing import List


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:

        siteroute = collections.defaultdict(list)

        for index, route in enumerate(routes):
            for site in route:
                siteroute[site].append(index)

        dis={source:0}

        q = collections.deque([source])

        while q:
            current = q.popleft()

            if current == target:
                break

            for bus in siteroute[current]:
                if routes[bus]:
                    for site in routes[bus]:
                        if site not in dis:
                            dis[site] = dis[current]+1
                            q.append(site)

                    routes[bus]=None

        return dis[target] if target in dis else -1


import math
from collections import defaultdict, deque
from typing import List


class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) ->List[str]:
        n = len(friends)
        g = [[] for i in range(n)]

        for index,neighbor in enumerate(friends):
            for u in neighbor:
                g[index].append(u)
        videos=defaultdict(int)
        visited=set()
        # dist=[math.inf if i!=id else 0 for i in range(n)]
        q=deque([(id,0)])
        visited.add(id)
        while q:
            cur,dis=q.popleft()
            if dis == level:
                for video in watchedVideos[cur]:
                    videos[video] += 1
                continue

            for u in g[cur]:
                if u not in visited:
                    if dis<level:
                        q.append((u,dis+1))
                        visited.add(u)


        sorted_dict=dict(sorted(videos.items(),key=lambda x:(x[1],x[0])))
        return list(sorted_dict.keys())






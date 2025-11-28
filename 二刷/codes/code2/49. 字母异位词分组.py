from typing import List
import collections

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        cnt=collections.defaultdict(list)

        for s in strs:
            key=''.join(sorted(s))
            cnt[key].append(s)

        return list(cnt.values())
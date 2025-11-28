import collections
from typing import List


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n=len(accounts)
        accandindex=collections.defaultdict(list)

        for index,li in enumerate(accounts):
            for email in li[1:]:
                accandindex[email].append(index)

        def dfs(v)->None:
            nonlocal visited,emails
            visited.add(v)

            for email in accounts[v][1:]:
                if email not in visited:
                    emails.add(email)
                    for index in accandindex[email]:
                        if index not in visited:
                            dfs(index)


        ans=[]
        visited = set()

        for index,li in enumerate(accounts):
            emails=set()
            if index not in visited:
                dfs(index)
                same=list(emails)
                same.sort()
                li2=[li[0]]
                li2.extend(same)
                ans.append(li2)

        return ans




accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]

print(Solution().accountsMerge(accounts))
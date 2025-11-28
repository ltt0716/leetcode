import collections
from typing import List, Dict


class Solution:
    def maxAmount(self, initialCurrency: str, pairs1: List[List[str]], rates1: List[float], pairs2: List[List[str]],
                  rates2: List[float]) -> float:
        def amount(initialCurrency,pairs,rates):

            adj=collections.defaultdict(list)

            for (v,u) ,rate in zip(pairs,rates):
                adj[v].append((u,rate))
                adj[u].append((v,1/rate))

            cash_amount={}
            now=1.0

            def dfs(v:str,now:float):
                cash_amount[v]=now

                for neighbor in adj[v]:
                    if neighbor[0] not in cash_amount.keys():
                        now=neighbor[1]*cash_amount[v]
                        dfs(neighbor[0],now)

            dfs(initialCurrency,now)

            return  cash_amount

        cash_amount1=amount(initialCurrency,pairs1,rates1)
        cash_amount2=amount(initialCurrency,pairs2,rates2)

        print(cash_amount1,cash_amount2)
        def cashmax(cash1:dict,cash2:dict):
            maxamount=1.0

            for key,val in cash1.items():
                if key in cash2.keys():
                    maxamount=max(maxamount,val/cash2[key])


            return maxamount

        return cashmax(cash_amount1,cash_amount2)





initialCurrency ="DXS"
pairs1 =[["F","QX"],["DXS","DBX"],["DXS","F"]]
rates1 =[2.7,5.7,4.6]
pairs2 =[["F","QX"],["F","DXS"],["DBX","F"]]
rates2 =[2.2,4.4,2.7]

print(Solution().maxAmount(initialCurrency,pairs1,rates1,pairs2,rates2))
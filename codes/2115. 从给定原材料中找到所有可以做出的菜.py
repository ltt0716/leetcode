from collections import defaultdict, deque
from typing import List


class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph=defaultdict(list)
        indegree=defaultdict(int)

        for index,items in enumerate(ingredients):
            for item in items:
                graph[item].append(recipes[index])
                indegree[recipes[index]]+=1

        q=deque([])
        ans=[]

        # print(graph,indegree)

        for item in supplies:
            q.append(item)

        while q:
            current=q.popleft()

            for item in graph[current]:
                indegree[item] -= 1
                if indegree[item]==0:
                    q.append(item)
                    ans.append(item)


        return ans

recipes = ["bread"]
ingredients = [["yeast","flour"]]
supplies = ["yeast","flour","corn"]

print(Solution().findAllRecipes(recipes, ingredients, supplies))
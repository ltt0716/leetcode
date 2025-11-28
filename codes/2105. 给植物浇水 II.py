from typing import List


class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        n=len(plants)

        l,r,ans=0,n-1,0
        wa,wb=capacityA,capacityB

        while l<=r:
            if l==r:
                if wa>=wb:
                    if plants[l]<=wa:
                        break
                    else:
                        wa=capacityA
                        ans+=1
                        break
                else:
                    if plants[l]<=wb:
                        break
                    else:
                        wb=capacityB
                        ans+=1
                        break

            if plants[l]<=wa:
                wa-=plants[l]
                l+=1
            else:
                wa=capacityA
                wa-=plants[l]
                ans+=1
                l+=1

            if plants[r]<=wb:
                wb-=plants[r]
                r-=1
            else:
                wb=capacityB
                wb-=plants[r]
                ans+=1
                r-=1
        return ans

plants =[1,2,4,4,5]
capacityA =6
capacityB =5

print(Solution().minimumRefill(plants, capacityA, capacityB))
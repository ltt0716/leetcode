class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n=len(strs)

        ans=[]
        cnt={}
        index=0

        for str in strs:
            tep={}
            for c in str:
                if c in tep.keys():
                    tep[c]+=1
                else:
                    tep[c]=1
            flag=0
            for key,val in cnt.items():
                if tep ==val:
                    ans[key].append(str)
                    flag=1
                    break
            
            if not flag:
                ans.append([str])
                cnt[index]=tep
                index+=1
        return ans

            
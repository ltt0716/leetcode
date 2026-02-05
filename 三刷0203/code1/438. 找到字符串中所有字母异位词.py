class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        m,n=len(p),len(s)
        mp=collections.defaultdict(int)

        for i in p:
            mp[i]+=1

        ans=[]
        l,r=0,0
        while r<n:
            c=s[r]
            r+=1

            if c in mp.keys():
                mp[c]-=1
            if r-l<m:
                continue

            if max(mp.values())==0:
                ans.append(l)

            if s[l] in mp.keys():
                mp[s[l]]+=1
            
            l+=1
            

        return ans

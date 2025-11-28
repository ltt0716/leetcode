import collections


class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        n=len(word1)

        d2=collections.defaultdict(int)

        l=r=ans=0

        for i in range(len(word2)):
            d2[word2[i]]+=1

        while r<n:
            ch=word1[r]
            if ch in word2:
                d2[ch]-=1

            while max(d2.values())<=0:
                c=word1[l]
                if c in word2:
                    d2[c]+=1
                l+=1
            ans+=l
            r+=1
        return ans

word1 ="abcabc"
word2 ="abc"
print(Solution().validSubstringCount(word1,word2))

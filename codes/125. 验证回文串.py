class Solution:
    def isPalindrome(self, s: str) -> bool:

        n=len(s)
        l,r=0,n-1

        while l<r:
           if s[l].isalnum()==False:
               l+=1
               continue

           if s[r].isalnum()==False:
               r-=1
               continue


           if s[l].lower()==s[r].lower():
                l+=1
                r-=1
           else:
               return False

        return True


s = "A man, a plan, a canal: Panama"
Solution().isPalindrome(s)
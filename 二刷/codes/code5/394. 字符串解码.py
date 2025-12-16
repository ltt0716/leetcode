class Solution:
    def decodeString(self, s: str) -> str:
        
        curstr=""
        curnum=0
        stack=[]

        for ch in s:
            if '9'>=ch>='0':
                curnum=curnum*10+int(ch)
            elif ch=='[':
                stack.append((curnum,curstr))
                curstr=""
                curnum=0
            elif ch==']':
                num,str=stack.pop()
                curstr=str+num*curstr
            else:
                curstr+=ch
        return curstr
                
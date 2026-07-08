class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if n==0:
            return 0
        s=0
        x=''
        st=str(n)
        for i in st:
            if i!='0':
                x+=i
                s+=int(i)
        x=int(x)
        return x*s
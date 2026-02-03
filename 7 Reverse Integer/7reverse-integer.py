class Solution:
    def reverse(self, x: int) -> int:
        n=True
        if x<0:
            n=False
            x=-1*x
        x=str(x)
        x=x[::-1]
        x=int(x)
        if x>(2**31-1) or x<(-1*2**31):
            x=0
        if n==False:
            x=-1*x
        return x
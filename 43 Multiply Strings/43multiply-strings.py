class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        a=b=0
        for i in num1:
            i=int(i)
            a=a*10+i
        for i in num2:
            i=int(i)
            b=b*10+i
        prod=a*b
        prod=str(prod)
        return prod
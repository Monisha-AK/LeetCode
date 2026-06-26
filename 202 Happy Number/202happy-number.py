class Solution:
    def isHappy(self, n: int) -> bool:
        s=[]
        sum=0
        while (n!=1):
            if sum not in s:
                s.append(sum)
            else:
                return False
            sum=0
            while(n>0):
                r=n%10
                sum+=r*r
                n//=10
            n=sum
        return True
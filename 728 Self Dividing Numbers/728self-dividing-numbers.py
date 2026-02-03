class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        s=[]
        for i in range(left,right+1):
            f=True
            for j in str(i):
                j=int(j)
                
                if j==0:
                    f=False
                    break
                elif i%j==0:
                    continue
                else:
                    f=False
            if f==True:
                s.append(i)
        return s
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        l=[]
        for i in range(numRows):
            m=[]
            for j in range(i):
                if(j==0):
                    c=1
                    m.append(c)
                else:
                    c=int((c*(i-j+1))/j)
                    m.append(c)
            m.append(1)
            l.append(m)
        return l
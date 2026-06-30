class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        l=[]
        for i in range(rowIndex):
            if i==0:
                c=1
                l.append(c)
            else:
                c=(c*(rowIndex-i+1))/i
                l.append(int(c))
        l.append(1)
        return l
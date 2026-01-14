class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s=0
        for i in digits:
            s=s*10+i
        s+=1
        s=str(s)
        new=[]
        for i in s:
            new.append(int(i))
        return new
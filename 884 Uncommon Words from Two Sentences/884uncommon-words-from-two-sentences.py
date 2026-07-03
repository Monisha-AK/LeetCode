class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s=s1+" "+s2
        l=[]
        d={}
        s=s.split()
        for i in s:
            d[i]=s.count(i)
        for i in d:
            if d[i]==1:
                l.append(i)
        return l
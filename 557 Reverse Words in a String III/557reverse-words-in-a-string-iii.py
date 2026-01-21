class Solution:
    def reverseWords(self, s: str) -> str:
        l=s.split()
        r=[]
        for i in l:
            i=i[::-1]
            r.append(i)
        sen=""
        for i in r:
            sen+=i
            sen+=" "
        return sen[:-1]
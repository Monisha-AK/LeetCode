class Solution:
    def vowelConsonantScore(self, s: str) -> int:
        import string
        c=v=0
        vow={'a','e','i','o','u'}
        for i in s:
            if i in vow:
                v+=1
            elif i in string.ascii_lowercase and i not in vow:
                c+=1
        if c==0:
            return 0
        return v//c

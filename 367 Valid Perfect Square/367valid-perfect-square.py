class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        s=(num)**0.5
        s1=int(s)
        if s==s1:
            return True
        else:
            return False

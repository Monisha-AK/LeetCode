class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l=s.split()
        le=len(l[-1])
        return le
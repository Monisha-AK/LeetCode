class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        c=0
        l=sorted(heights)
        for i in range(len(heights)):
            if l[i]!=heights[i]:
                c+=1
        return c
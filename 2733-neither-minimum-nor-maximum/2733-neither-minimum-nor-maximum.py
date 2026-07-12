class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        s = sorted(set(nums))
        if len(s)<=2:
            return -1
        else:
            return s[1]
        
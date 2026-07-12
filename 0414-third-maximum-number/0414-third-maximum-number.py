class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        s = sorted(set(nums))
        if len(s)<3:
            return max(s)
        else:
            return s[-3]
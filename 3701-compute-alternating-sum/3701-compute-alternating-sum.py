class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if i%2!=0:
                nums[i]*=-1
        return sum(nums)
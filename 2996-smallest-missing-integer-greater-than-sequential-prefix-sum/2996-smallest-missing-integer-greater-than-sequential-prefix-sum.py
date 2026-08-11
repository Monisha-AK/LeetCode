class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        s=0
        i=1
        while(i<len(nums) and nums[i] == nums[i - 1] + 1):
            i+=1
        for j in range(0,i):
            s+=nums[j]
        while True:
            if (s in nums):
                s+=1
            else:
                break
        return s
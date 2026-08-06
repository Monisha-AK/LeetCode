class Solution {
    public int dominantIndex(int[] nums) {
        int max=nums[0],i=0,j;
        for (j=1;j<nums.length;j++){
            if(nums[j]>max){
                max=nums[j]; 
                i=j;
                }
        }
        for(j=0;j<nums.length;j++){
            if(i!=j){
               if (nums[i]>=2*nums[j])
                continue;
            else
                return -1;  
            }
            
        }
        return i;
    }
}
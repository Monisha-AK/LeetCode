class Solution {
    public int[] runningSum(int[] nums) {
        int[] res=new int[nums.length];
        int c=0;
        for (int i=0;i<nums.length;i++){
            c+=nums[i];
            res[i]=c;
        }
        return res;
    }
}
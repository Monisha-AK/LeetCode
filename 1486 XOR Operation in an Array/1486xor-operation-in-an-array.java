class Solution {
    public int xorOperation(int n, int start) {
        int x=0,i;
        for (i=0;i<n;i++){
            x=x^(start+2*i);
        }
        return x;
    }
}
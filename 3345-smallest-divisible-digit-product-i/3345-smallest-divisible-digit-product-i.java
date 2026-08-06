class Solution {
    public int smallestNumber(int n, int t) {
        while(true){
            int i=n,p=1;
            while(i>0){
                p*=(i%10);
                i/=10;
            }
            if (p%t==0)
                return n;
            n++;
        }
    }
}
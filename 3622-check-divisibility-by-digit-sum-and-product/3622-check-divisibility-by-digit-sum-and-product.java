class Solution {
    public boolean checkDivisibility(int n) {
        int s=0,p=1,r,num=n;
        while(n>0){
            r=n%10;
            s+=r;
            p*=r;
            n=n/10;
        }
        return (num%(s+p)==0);
    }
}
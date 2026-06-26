class Solution {
    public int numberOfMatches(int n) {
        int m=0,a=0,t=0;
        while(n>1){
            if(n%2==0){
            m=n/2;
            a=n/2;
        }
        else{
            m=(n-1)/2;
            a=((n-1)/2)+1;
        }
        n=a;
        t=t+m;
    }
    return t;
    }
}
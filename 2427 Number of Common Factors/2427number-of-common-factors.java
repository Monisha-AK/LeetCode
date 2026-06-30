class Solution {
    public int commonFactors(int a, int b) {
        int r,i,c=0;
        while (b>0){
            r=a%b;
            a=b;
            b=r;
        }
        for(i=1;i<=a;i++){
            if(a%i==0){c++;}
        }
        return c;
    }
}
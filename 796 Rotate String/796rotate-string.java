class Solution {
    public boolean rotateString(String s, String goal) {
        boolean x=true;
        if(s.length()!=goal.length()){
                x=false;
                return x;
        }
        String s1=s.concat(s);
        x=s1.contains(goal);
        return x;
    }
}
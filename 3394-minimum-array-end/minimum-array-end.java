class Solution {
    public long minEnd(int n, int x) {
        long ans = x;
        while(n-- > 1){
            ans = (ans+1) | x;
        }   

        return ans;
    }
}
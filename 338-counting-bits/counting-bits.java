class Solution {
    public int[] countBits(int n) {
        int[] res = new int[n+1];
        for(int i =0;i<=n;i++){
            int ans = countBit(i);
            res[i] = ans;
        }
        return res;
    }

    public int countBit(int n){
        int count = 0;
        while (n != 0){
            count++;
            n &= n - 1;
        }
        return count;
    }
}
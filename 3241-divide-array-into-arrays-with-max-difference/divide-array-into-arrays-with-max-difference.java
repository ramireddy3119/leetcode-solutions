class Solution {
    public int[][] divideArray(int[] nums, int k) {
        Arrays.sort(nums);
        int n = nums.length/3;
        int[][] res = new int[n][3]; 
        int row = 0;
        for(int i = 0; i < nums.length;i+=3){
            // if(i+2 >= nums.length) return new int[0][0];
            int a = nums[i];
            int b = nums[i+1];
            int c = nums[i+2];
            if((c - a) > k) return new int[0][0];
            res[row][0] = a;
            res[row][1] = b;
            res[row][2] = c;
            row++;
        }
        return res;
    }
}
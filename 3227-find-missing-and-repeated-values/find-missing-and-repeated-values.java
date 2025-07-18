class Solution {
    public int[] findMissingAndRepeatedValues(int[][] grid) {
        Map<Integer,Integer> mpp = new HashMap<>();
        int summ = 0;
        int repeat = -1;
        for(int i = 0;i < grid.length;i++){
            for(int j = 0;j<grid[0].length;j++){
                if(mpp.containsKey(grid[i][j]))
                    repeat = grid[i][j];
                summ += grid[i][j];
                mpp.put(grid[i][j],mpp.getOrDefault(grid[i][j],0)+1);
            }
        }
        int n = grid.length * grid[0].length;
        int totSum = n*(n+1) / 2;
        if (summ > totSum){
           int rem = summ - totSum;
            return new int[] {repeat,repeat-rem};
        }else{
            int rem = totSum - summ;
            return new int[] {repeat,repeat+rem};
        }
    }
}
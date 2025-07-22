class Solution {
    public int maximumUniqueSubarray(int[] nums) {
        Map<Integer,Integer> map = new HashMap<>();
        int left = 0;
        int right = 0;
        int maxSum = -1;
        int currSum = 0;
        for(int i =0;i < nums.length; i++){
            currSum += nums[i];
            map.put(nums[i],map.getOrDefault(nums[i],0)+1);
            int count = map.get(nums[i]);
            while(count > 1){
                currSum -= nums[left];
                map.remove(nums[left]);
                if(map.get(nums[left]) == map.get(nums[i])){
                    count --;
                }
                left++;
            }
            map.put(nums[i],count);
            maxSum = Math.max(maxSum,currSum);
        }
        return maxSum;
    }
}
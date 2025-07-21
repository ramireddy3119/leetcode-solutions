import java.util.Arrays;

class Solution {
    public int numSubseq(int[] nums, int target) {
        int MOD = 1_000_000_007;
        int n = nums.length;
        Arrays.sort(nums);

        // Precompute powers of 2
        int[] pow = new int[n];
        pow[0] = 1;
        for (int k = 1; k < n; k++) {
            pow[k] = (pow[k - 1] * 2) % MOD;
        }

        int i = 0, j = n - 1;
        int count = 0;

        while (i <= j) {
            if (nums[i] + nums[j] <= target) {
                count = (count + pow[j - i]) % MOD;
                i++;
            } else {
                j--;
            }
        }

        return count;
    }
}

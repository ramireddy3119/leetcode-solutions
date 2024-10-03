class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total_sum = sum(nums)
        target = total_sum % p
        if target == 0:
            return 0
        
        prefix_mod = 0
        min_len = len(nums)
        mod_map = {0:-1}

        for i, num in enumerate(nums):
            prefix_mod = (prefix_mod + num) % p
            mod_map[prefix_mod] = i

            needed_mod = (prefix_mod - target) % p
            if needed_mod in mod_map:
                min_len = min(min_len, i - mod_map[needed_mod])
        return min_len if min_len < len(nums) else -1
        
from collections import defaultdict

class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        count = 0
        prefix = 0
        freq = defaultdict(int)
        freq[0] = 1

        for num in nums:
            if num % modulo == k:
                prefix += 1
            mod_val = prefix % modulo
            target = (mod_val - k + modulo) % modulo
            count += freq[target]
            freq[mod_val] += 1

        return count

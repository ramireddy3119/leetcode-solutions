from typing import List

class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        odd_count = 0  
        even_count = 1 
        prefix_sum = 0
        count = 0

        for num in arr:
            prefix_sum += num
            if prefix_sum % 2 == 0:
                count = (count + odd_count) % MOD
                even_count += 1
            else:
                count = (count + even_count) % MOD
                odd_count += 1

        return count

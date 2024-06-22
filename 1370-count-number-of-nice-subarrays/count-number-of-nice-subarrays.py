class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def atMost(k: int) -> int:
            count = 0
            left = 0
            for right in range(len(nums)):
                if nums[right] % 2 == 1:
                    k -= 1
                while k < 0:
                    if nums[left] % 2 == 1:
                        k += 1
                    left += 1
                count += right - left + 1
            return count
        
        return atMost(k) - atMost(k - 1)

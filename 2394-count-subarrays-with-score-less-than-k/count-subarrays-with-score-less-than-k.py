class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        count = 0
        score = 0
        left = 0
        length = 0
        for right in range(len(nums)):
            score += nums[right]
            length += 1
            while score * length >= k and left <= right:
                score -= nums[left]
                left += 1
                length -= 1
            count += (right - left + 1)
        return count
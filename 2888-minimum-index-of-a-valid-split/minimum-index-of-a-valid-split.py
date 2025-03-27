class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        counter = Counter(nums)
        dominant, freq = counter.most_common(1)[0]
        
        left_count = 0
        right_count = freq
        
        for i in range(len(nums) - 1):
            if nums[i] == dominant:
                left_count += 1
                right_count -= 1
            
            if left_count * 2 > (i + 1) and right_count * 2 > (len(nums) - i - 1):
                return i 
        
        return -1 

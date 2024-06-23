class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        minDeque = deque()
        maxDeque = deque()
        left = 0
        maxLen = 0
    
        for right in range(len(nums)):
            while minDeque and nums[right] < nums[minDeque[-1]]:
                minDeque.pop()
            while maxDeque and nums[right] > nums[maxDeque[-1]]:
                maxDeque.pop()
        
            minDeque.append(right)
            maxDeque.append(right)
        
            if nums[maxDeque[0]] - nums[minDeque[0]] > limit:
                if minDeque[0] == left:
                    minDeque.popleft()
                if maxDeque[0] == left:
                    maxDeque.popleft()
                left += 1
        
            maxLen = max(maxLen, right - left + 1)
    
        return maxLen


        
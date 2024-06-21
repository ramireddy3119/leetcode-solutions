class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        num_counts = defaultdict(int)
        
        for num in nums:
            count += num_counts[num]
            num_counts[num] += 1
        
        return count
        
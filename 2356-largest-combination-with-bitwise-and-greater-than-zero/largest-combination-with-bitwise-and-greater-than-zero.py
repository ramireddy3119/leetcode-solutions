class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        maxCombination = 0

        for i in range(30):
            count = 0
            for num in candidates:
                if num & (1<<i) != 0:
                    count += 1
            maxCombination = max(maxCombination,count)
        
        return maxCombination
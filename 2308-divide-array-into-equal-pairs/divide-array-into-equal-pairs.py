class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        counter = Counter(nums)
        for i in counter.values():
            if i % 2 != 0:
                return False
        return True
        
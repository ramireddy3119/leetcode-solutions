class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        nums.sort(key=lambda x: (count[x], -x))
        return nums
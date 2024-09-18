class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        res = [item for item,count in freq.most_common(k)]
        return res
        
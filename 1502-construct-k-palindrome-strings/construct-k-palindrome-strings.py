class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
        counter = Counter(s)
        odd_count = sum(1 for count in counter.values() if count % 2 != 0)
        return odd_count <= k


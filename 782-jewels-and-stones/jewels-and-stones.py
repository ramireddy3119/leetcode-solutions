class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        num = 0
        jewels = set(jewels)
        for s in stones:
            if s in jewels:
                num += 1
        return num
        
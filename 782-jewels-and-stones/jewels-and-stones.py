class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        num = 0
        for s in stones:
            if s in jewels:
                num += 1
        return num
        
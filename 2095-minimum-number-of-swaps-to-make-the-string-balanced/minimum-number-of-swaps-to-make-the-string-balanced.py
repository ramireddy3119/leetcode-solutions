class Solution:
    def minSwaps(self, s: str) -> int:
        max_imbalance = 0
        imbalance = 0
        for i in s:
            if i == ']':
                imbalance += 1
            else:
                imbalance -= 1
            max_imbalance = max(max_imbalance,imbalance)
        return (max_imbalance+1)//2

                
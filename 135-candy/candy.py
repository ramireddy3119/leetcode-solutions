class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        left = [1]*n
        right = [1]*n
        for i in range(1,n):
            if ratings[i] > ratings[i-1]:
                left[i] = left[i-1] + 1
        for j in range(n-2,-1,-1):
            if ratings[j] > ratings[j+1]:
                right[j] = right[j+1] + 1
        res = sum(max(left[i],right[i]) for i in range(n))
        return res

        
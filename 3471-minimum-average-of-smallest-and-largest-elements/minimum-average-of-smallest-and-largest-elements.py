class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        n = len(nums)//2
        average = []
        for i in range(n):
            maxEle = max(nums)
            minEle = min(nums)
            nums.remove(maxEle)
            nums.remove(minEle)
            avg = (maxEle + minEle)/2
            average.append(avg)
        return min(average)

            
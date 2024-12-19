class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        count = 0
        maxi = 0
        for i in range(len(arr)):
            maxi = max(maxi,arr[i])
            if maxi == i:
                count += 1
        return count
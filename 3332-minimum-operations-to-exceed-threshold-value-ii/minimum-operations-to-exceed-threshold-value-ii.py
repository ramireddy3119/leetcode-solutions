class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        minheap = []
        for num in nums:
            heapq.heappush(minheap,num)
        count = 0
        while minheap:
            min1 = heapq.heappop(minheap)
            if min1 >= k:
                break
            min2 = heapq.heappop(minheap)
            count += 1
            heapq.heappush(minheap,2*min(min1,min2)+max(min1,min2))
        return count
        
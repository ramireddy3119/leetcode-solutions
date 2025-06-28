class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        indx = [(num,i) for i,num in enumerate(nums)]
        top_k = heapq.nlargest(k, indx, key = lambda x:x[0])
        top_k.sort(key=lambda x:x[1])
        return [num for num,i in top_k]
        
        
class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        def noOfStores(mid):
            count = 0
            for i in quantities:
                count += ceil(i/mid)
            return count <= n


        low =  1
        high = max(quantities)
        ans = float('inf')
        while low <= high:
            mid = low + (high-low)//2
            if noOfStores(mid):
                ans = min(ans,mid)
                high = mid - 1
            else:
                low = mid + 1
        return ans 
            

        
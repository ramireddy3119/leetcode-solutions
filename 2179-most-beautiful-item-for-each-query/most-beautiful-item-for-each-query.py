from typing import List

class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        def binarySearch(items, price):
            l = 0
            r = len(items) - 1
            maxi = 0
            while l <= r:
                mid = l + (r - l) // 2
                if items[mid][0] <= price:
                    maxi = max(maxi, items[mid][1])
                    l = mid + 1  
                else:
                    r = mid - 1  
            return maxi

        items.sort()
       
        for i in range(1, len(items)):
            items[i][1] = max(items[i - 1][1], items[i][1])

        res = []

        for price in queries:
            max_beauty = binarySearch(items, price)
            res.append(max_beauty)
        
        return res

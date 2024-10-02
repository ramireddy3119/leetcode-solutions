class Solution:
    def arrayRankTransform(self,arr):
        sorted_arr = sorted(set(arr))
        rank_dict = {val: rank + 1 for rank, val in enumerate(sorted_arr)}  
    
        return [rank_dict[val] for val in arr]  

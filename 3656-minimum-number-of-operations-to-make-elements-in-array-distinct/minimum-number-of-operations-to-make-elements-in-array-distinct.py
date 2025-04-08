class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        seen = set()
        for i in range(len(nums)-1,-1,-1):
            if nums[i] not in seen:
                seen.add(nums[i])
            else:
                return (i//3)+1
        return 0
         

        
        

        
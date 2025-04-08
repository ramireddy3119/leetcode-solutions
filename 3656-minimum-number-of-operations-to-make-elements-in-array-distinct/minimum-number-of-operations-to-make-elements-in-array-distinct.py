class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        def isDistinct(arr):
            hashmap = {}
            for num in arr:
                if num in hashmap:
                    hashmap[num] += 1
                else:
                    hashmap[num] = 1
            return all(value == 1 for value in hashmap.values())
            
        if isDistinct(nums):
            return 0
        count = 1
        for i in range(3,len(nums),3):
            if isDistinct(nums[i:]):
               return count
            else:
                count += 1

        return count
         

        
        

        
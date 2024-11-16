class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        
        n = len(nums)
        res = []
        for i in range(n-k+1):
            flag = True
            current = nums[i]
            for j in range(i+1,i+k):
                if nums[j] != nums[j-1] + 1:
                    flag = False
                    break
                current = max(current,nums[j])
            if flag:
                res.append(current)
            else:
                res.append(-1)
        return res
        
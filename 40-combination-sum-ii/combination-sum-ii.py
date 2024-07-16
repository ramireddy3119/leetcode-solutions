class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def helper(ind,arr,tar,res,ds):
            if tar == 0:
                res.append(list(ds))
                return 
            for i in range(ind,len(arr)):
                if i>ind and arr[i] == arr[i-1]:continue
                if arr[i] > tar:break
                ds.append(arr[i])
                helper(i+1,arr,tar-arr[i],res,ds)
                ds.pop()
        res = []
        candidates.sort()
        helper(0,candidates,target,res,[])
        return res

        
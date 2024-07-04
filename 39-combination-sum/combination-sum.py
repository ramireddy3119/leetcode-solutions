class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def helper(ind,arr,tar,res,ds):
            if ind == len(arr):
                if tar == 0:
                    res.append(list(ds))
                return 
            if arr[ind] <= tar:
                ds.append(arr[ind])
                helper(ind,arr,tar-arr[ind],res,ds)
                ds.pop()
            helper(ind+1,arr,tar,res,ds)
        res = []
        helper(0,candidates,target,res,[])
        return res

        
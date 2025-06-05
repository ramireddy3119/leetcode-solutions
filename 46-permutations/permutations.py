class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def permutation(curr,rem):
            if not rem:
                res.append(curr[:])
                return
            for i in range(len(rem)):
                curr.append(rem[i])
                permutation(curr,rem[:i]+rem[i+1:])
                curr.pop()
        res = []
        permutation([],nums)
        return res


        
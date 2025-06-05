class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def combinations(start,curr):
            if len(curr) == k:
                res.append(curr[:])
            for i in range(start,n+1):
                curr.append(i)
                combinations(i+1,curr)
                curr.pop()
        res = []
        combinations(1,[])
        print(res)
        return res
            
        
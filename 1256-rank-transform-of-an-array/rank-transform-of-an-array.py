class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        temp_arr = sorted(arr)
        mpp = {}
        count = 1
        for num in temp_arr:
            if num not in mpp:
                mpp[num] = count
                count += 1
        res = []
        for i in range(len(arr)):
            res.append(mpp[arr[i]])
        return res



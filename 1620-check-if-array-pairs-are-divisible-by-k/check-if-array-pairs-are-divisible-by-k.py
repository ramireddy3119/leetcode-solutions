class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        if len(arr) % 2 != 0:
            return False
        
        mpp = {}
        for i in range(len(arr)):
            rem = arr[i] % k
            if rem < 0:
                rem = rem + k
            if rem in mpp:
                mpp[rem] += 1
            else:
                mpp[rem] = 1
        
        for rem,count in mpp.items():
            if rem == 0:
                if count % 2 != 0:
                    return False
            else:
                complement = k - rem
                if complement not in mpp or mpp[rem] != mpp[complement]:
                    return False
        return True
        
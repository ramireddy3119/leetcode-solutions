class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        mapp = {}
        for i in nums:
            if  i in mapp:
                return True
            mapp[i] = True
        return False
        
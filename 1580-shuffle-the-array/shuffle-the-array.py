class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        arr = []
        count = 2*n
        i = 0
        while count:
            arr.append(nums[i])
            i += 1
            arr.append(nums[n])
            n += 1
            count -= 2
        return arr

        
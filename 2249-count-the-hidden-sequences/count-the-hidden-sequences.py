class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        min_val = 0
        max_val = 0
        curr_val = 0
        for i in differences:
            curr_val += i
            if curr_val > max_val:
                max_val = curr_val
            if curr_val < min_val:
                min_val = curr_val
        count = (upper-lower)-(max_val - min_val) + 1
        return count if count > 0 else 0
        
class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        min_val = 0
        max_val = 0
        curr_val = 0
        for i in differences:
            curr_val += i
            max_val = max(max_val,curr_val)
            min_val = min(min_val,curr_val)
        count = (upper-lower)-(max_val - min_val) + 1
        return count if count > 0 else 0
        
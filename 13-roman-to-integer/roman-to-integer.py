class Solution:
    def romanToInt(self, s: str) -> int:
        roman_numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
        }
        num = 0
        prev_value = 0
        for i in s:
            value = roman_numerals[i]
            if value > prev_value:
                num += value - 2 * prev_value
            else:
                num += value
            prev_value = value
        return num
        
        
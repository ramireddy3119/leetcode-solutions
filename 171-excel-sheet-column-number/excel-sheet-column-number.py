class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        column = 0
        for i in columnTitle:
            column = column * 26 + ord(i)-64
        return column

        
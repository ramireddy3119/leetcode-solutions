class Solution:
    def intToRoman(self, num: int) -> str:
        mpp = {
            1000:"M", 900:"CM", 500:"D", 400 :"CD", 100:"C", 90:"XC",
            50:"L", 40:"XL", 10 :"X", 9: "IX", 5:"V",4:"IV",1:"I"
        }

        res = ""
        for value in mpp.keys():
            while num >= value:
                res += mpp[value]
                num -= value
        
        return res
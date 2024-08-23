class Solution:
    def defangIPaddr(self, address: str) -> str:
        str1 = address.replace('.','[.]')
        return str1
        
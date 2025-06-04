class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arr = [0]*26
        for i in range(len(s)):
            arr[ord(s[i])-97] += 1
        for j in range(len(t)):
            arr[ord(t[j])-97] -= 1
        return all(x == 0 for x in arr)
        
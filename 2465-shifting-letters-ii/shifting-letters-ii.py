class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        arr = [0]*(len(s)+1)
        for l,r,d in shifts:
            if d == 0:
                arr[l] -= 1
                arr[r+1] += 1
            else:
                arr[l] += 1
                arr[r+1] -= 1
        for i in range(1,len(arr)):
            arr[i] += arr[i-1]
        res = ""
        for i in range(len(arr)-1):
            ltr = s[i]
            res += chr((ord(ltr) - ord('a') + arr[i]) % 26 + ord('a'))

        return res
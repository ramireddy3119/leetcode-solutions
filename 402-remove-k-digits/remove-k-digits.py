class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        st = []
        for i in range(len(num)):
            while st and k > 0 and st[-1] > num[i]:
                st.pop()
                k -= 1
            st.append(num[i])
        
        while k > 0:
            st.pop()
            k -= 1
        res = ''.join(st)
        res = res.lstrip('0')
        return res if res else "0"

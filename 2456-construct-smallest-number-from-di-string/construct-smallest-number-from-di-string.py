class Solution:
    def smallestNumber(self, pattern: str) -> str:
        st = []
        res = ""
        i = 1
        
        for c in pattern:
            st.append(i)
            i += 1
            if c == 'I':
                while st:
                    res += str(st.pop())
        
        st.append(i)
        while st:
            res += str(st.pop())

        return res

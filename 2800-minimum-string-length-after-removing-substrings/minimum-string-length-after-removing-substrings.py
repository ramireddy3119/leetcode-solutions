class Solution:
    def minLength(self, s: str) -> int:
        st = []
        for char in s:
            st.append(char)
            if len(st) >= 2 and ((st[-1] == "B" and st[-2]=="A") or (st[-1] == "D" and st[-2]=="C")):
                st.pop()
                st.pop()
        return len(st)
                
        
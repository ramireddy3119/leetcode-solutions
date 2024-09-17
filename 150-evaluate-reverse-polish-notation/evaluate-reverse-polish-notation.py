class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for i in tokens:
            if i in '+-*/':
                if i == '+':
                    a,b = st.pop(),st.pop()
                    st.append(a + b)
                elif i == '-':
                    a,b = st.pop(),st.pop()
                    st.append(b - a)
                elif i == '*':
                    a,b = st.pop(),st.pop()
                    st.append(a * b)
                elif i == '/':
                    a,b = st.pop(),st.pop()
                    st.append(int(b/ a))
            else:
                st.append(int(i))
        
        return st[0]

        
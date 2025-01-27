class Solution:
    def longestValidParentheses(self, s: str) -> int:
        st = [-1] 
        curr = 0
        maxi = 0
        for i in range(len(s)):
            if s[i] == ')':
                st.pop()
                if len(st) == 0:
                    st.append(i)
                    continue
                curr = i - st[-1]
            else:
                st.append(i)
            maxi = max(maxi,curr)
        return maxi
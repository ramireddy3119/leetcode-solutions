class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def removePairs(s,a,b,score):
            st = []
            points = 0
            for i in s:
                if st and st[-1] == a and b == i:
                    points += score
                    st.pop()
                else:
                    st.append(i)
            return ''.join(st),points
        if x > y:
            s,points1 = removePairs(s,'a','b',x)
            _,points2 = removePairs(s,'b','a',y)
        else:
            s,points1 = removePairs(s,'b','a',y)
            _,points2 = removePairs(s,'a','b',x)

        return points1+ points2
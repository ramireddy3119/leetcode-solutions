class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        s = {}
        for i in range(len(names)):
            s[heights[i]]=names[i]
        heights.sort(reverse = True)
        for ind in range(len(names)):
            h = heights[ind]
            names[ind] = s[h]
        return names
            
                    

        
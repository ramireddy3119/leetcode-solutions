class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        res = []
        # for i in queries:
        #     count = 0
        #     for j in range(i[0],i[-1]+1):
        #         word = words[j]
        #         if word[0].lower() in "aeiou" and word[-1].lower() in "aeiou":
        #             count += 1
        #     res.append(count)
        prefix_sum = [0]*len(words)
        word = words[0]
        if word[0].lower() in "aeiou" and word[-1].lower() in "aeiou":
            prefix_sum[0] = 1
        else:
            prefix_sum[0] = 0
        for i in range(1,len(words)):
            wrd = words[i]
            if wrd[0].lower() in "aeiou" and wrd[-1].lower() in "aeiou":
                prefix_sum[i] = prefix_sum[i-1]+1
            else:
                prefix_sum[i] = prefix_sum[i-1]
        for l,r in queries:
            if l == 0:
                res.append(prefix_sum[r])
            else:
                res.append(prefix_sum[r]-prefix_sum[l-1])
        return res

            


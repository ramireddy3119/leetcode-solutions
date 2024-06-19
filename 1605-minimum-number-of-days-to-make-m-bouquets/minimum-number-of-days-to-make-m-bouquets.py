class Solution:
    def findMax(self,bloomDay):
        maxi = float('-inf')
        for i in range(len(bloomDay)):
            maxi = max(maxi,bloomDay[i])
        return maxi
    def findMin(self,bloomDay):
        mini = float('inf')
        for i in range(len(bloomDay)):
            mini = min(mini,bloomDay[i])
        return mini
    def countMin(self,bloomDay,mid,m,k):
        n = len(bloomDay)
        count = 0
        noBq = 0
        for i in range(n):
            if bloomDay[i] <= mid:
                count += 1
            else:
                noBq += (count//k)
                count = 0 
        noBq += (count//k)
        if(noBq >= m):
            return True
        else:
            return False
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if m*k > n:
            return -1
        low = self.findMin(bloomDay)
        high = self.findMax(bloomDay)
        ans = high
        while(low <= high):
            mid = (low+high)//2
            if (self.countMin(bloomDay,mid,m,k))==True:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return low
                
       
        
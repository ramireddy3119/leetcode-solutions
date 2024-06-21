class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        maxSum = currChange = zeroSum = 0
        for i in range(len(customers)):
            if grumpy[i] == 0:
                zeroSum += customers[i]
            if grumpy[i] == 1:
                currChange += customers[i]
            if i >= minutes and grumpy[i-minutes]:
                currChange -= customers[i-minutes]
            maxSum = max(maxSum,currChange)
        return zeroSum + maxSum

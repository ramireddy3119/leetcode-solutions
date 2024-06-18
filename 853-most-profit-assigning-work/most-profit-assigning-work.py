class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = zip(difficulty,profit)
        sorted_jobs = sorted(jobs)
        sorted_workers = sorted(worker)

        j = total_profit = maxProfit = 0
        for i in sorted_workers:
            while j < len(sorted_workers) and i >= sorted_jobs[j][0]:
                maxProfit = max(maxProfit,sorted_jobs[j][1])
                j += 1
            
            total_profit += maxProfit
        
        return total_profit
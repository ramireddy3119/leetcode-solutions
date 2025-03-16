class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def noOfCars(mid):
            count = 0
            for i in ranks:
                c2 = mid/i
                c = floor(sqrt(c2))
                count += c
            return count >= cars
        low = 1
        high = max(ranks)* (cars*cars)
        while low < high:
            mid = (low + high)//2
            if noOfCars(mid):
                high = mid
            else:
                low = mid + 1
        return low
        
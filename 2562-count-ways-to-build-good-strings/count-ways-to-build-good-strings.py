class Solution:
    def countGoodStrings(self,low, high, zero, one):
        MOD = 10**9 + 7

        # Memoization dictionary
        memo = {}

        def count_ways(length):
            # Base cases
            if length == 0:
                return 1
            if length < 0:
                return 0

            # Check if already computed
            if length in memo:
                return memo[length]

            # Recursive calculation
            result = (count_ways(length - zero) + count_ways(length - one)) % MOD
            memo[length] = result
            return result

        # Sum the results for lengths in the range [low, high]
        total_ways = 0
        for length in range(low, high + 1):
            total_ways = (total_ways + count_ways(length)) % MOD

        return total_ways

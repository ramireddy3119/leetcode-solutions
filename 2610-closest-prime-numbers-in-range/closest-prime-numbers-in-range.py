class Solution:
    def closestPrimes(self,left: int, right: int):
        def sieve(n):
            is_prime = [True] * (n + 1)
            is_prime[0], is_prime[1] = False, False
            for i in range(2, int(n**0.5) + 1):
                if is_prime[i]:
                    for j in range(i * i, n + 1, i):
                        is_prime[j] = False
            return is_prime

        is_prime = sieve(right)

        primes = [i for i in range(left, right + 1) if is_prime[i]]

        if len(primes) < 2:
            return [-1, -1] 

        min_diff = float('inf')
        result = [-1, -1]
        
        for i in range(len(primes) - 1):
            if primes[i + 1] - primes[i] < min_diff:
                min_diff = primes[i + 1] - primes[i]
                result = [primes[i], primes[i + 1]]
        
        return result


        
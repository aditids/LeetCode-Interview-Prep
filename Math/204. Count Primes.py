# 204. Count Primes

class Solution:
    def countPrimes(self, n: int) -> int:
        if n<=2: return 0
        prime_numbers = [1]*n
        prime_numbers[0] = prime_numbers[1] = 0
        k = 2
        while k*k<n:
            if prime_numbers[k]==1:
                for i in range(k*k,n,k):
                    prime_numbers[i]=0
            k+=1          
        return sum(prime_numbers)

        # Used Sieve of Eratosthenes algorithm
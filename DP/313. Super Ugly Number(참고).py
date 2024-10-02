class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:

        minPQ = [] 

        for prime in primes:
            heapq.heappush(minPQ, (prime, 0, prime))

        output = [1]

        while len(output) < n:

            value, idx, prime = heapq.heappop(minPQ)

            if value != output[-1]:
                output.append(value)

            heapq.heappush(minPQ, (output[idx+1]*prime, idx+1, prime))
        
        return output[n-1]
        

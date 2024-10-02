from collections import deque

class Solution:

    def __init__(self):
        self.minTotal = 1e9 

    
    def bfs(self, src, dst, n, k, prices):

        q = deque()
        q.append([src, 0, 0])
        INF = 1e9
        visited = [INF]*(n+1)

        while q:
            curr, total, cnt = q.popleft()
            visited[curr] = total 

            if curr == dst:
                self.minTotal = min(self.minTotal, total)

            if cnt > k:
                continue

            for info in prices[curr]:
                end = info[0]
                price = info[1]
                if visited[end] > total+price:
                    q.append([end, total+price, cnt+1])

        return self.minTotal


    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        prices = [[] for _ in range(n)]

        for flight in flights:
            start = flight[0]
            end = flight[1]
            price = flight[2]
            prices[start].append([end, price])

        result = self.bfs(src, dst, n, k, prices)
        if result == 1e9:
            return -1 
        return result 

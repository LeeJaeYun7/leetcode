from collections import deque

class Solution:

    
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:

        dx = [0, 0, -1, 1]
        dy = [-1, 1, 0, 0]

        def isInside(x, y, m, n):
            if 0<=x and x<m and 0<=y and y<n:
                return True
            else:
                return False

        def bfs(x, y, grid, health):

            if health == 1 and grid[x][y] == 1:
                return False

            m = len(grid)
            n = len(grid[0])

            INF = -1e9
            count = [[INF]*n for _ in range(m)]

            q = deque()

            if grid[x][y] == 0:
                q.append([x, y, health])
                count[x][y] = health
            else:
                q.append([x, y, health-1])
                count[x][y] = health-1

            while q:

                x, y, health = q.popleft()
             
                if health == 0:
                    continue

                if x == m-1 and y == n-1:
                    return True

                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]

                    if isInside(nx, ny, m, n):

                        if grid[nx][ny] == 1 and (count[nx][ny] < health-1):
                            count[nx][ny] = health-1
                            q.append([nx, ny, health-1])
                        elif grid[nx][ny] == 0 and (count[nx][ny] < health):
                            count[nx][ny] = health
                            q.append([nx, ny, health])

            return False



        result = bfs(0, 0, grid, health)
        return result 
            

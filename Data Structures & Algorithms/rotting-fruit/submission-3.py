class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        if rows <= 0:
            return -1
        cols = len(grid[0])
        if cols <= 0:
            return -1
        
        queue = deque()
        freshFruits = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    freshFruits += 1
                elif grid[r][c] == 2:
                    queue.append((r,c))
        dire = [[0,1], [0,-1], [1,0], [-1,0]]
        timeToRotten = 0
        while queue:
            queueSize = len(queue)
            print(f"----- {timeToRotten}")
            for _ in range(queueSize):
                r, c = queue.popleft()
                print(f"{r}-{c}")
                for rd, cr in dire:
                    nr, nc = r+rd, c+cr
                    if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                        continue
                    
                    if grid[nr][nc] != 1:
                        continue
                    
                    freshFruits -= 1
                    queue.append((nr, nc))
                    grid[nr][nc] = 2

            timeToRotten += 1

        if freshFruits > 0:
            return -1
        if timeToRotten == 0:
            return timeToRotten
        return timeToRotten-1


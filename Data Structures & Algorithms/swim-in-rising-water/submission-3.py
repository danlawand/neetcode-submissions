class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = set()
        maxHeight = [[grid[0][0], 0, 0]]
        directions = [[-1,0], [1,0], [0,1], [0,-1]]
        while maxHeight:
            t, r, c = heapq.heappop(maxHeight)
            if r == n-1 and c == n-1:
                return t
            
            for rDir, cDir in directions:
                newR, newC = r+rDir, c+cDir
                if newR < 0 or newC < 0 or newR >= n or newC >= n or (newR, newC) in visited:
                    continue
                # O(n log n)
                heapq.heappush(maxHeight, [max(t, grid[newR][newC]), newR, newC])
                visited.add((newR, newC))
        return -1
            



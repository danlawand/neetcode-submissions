class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        minH = [[grid[0][0], 0, 0]]
        visited = set()
        visited.add((0,0))
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        while minH:
            t, r, c = heapq.heappop(minH)
            if r == n-1 and c == n-1:
                return t
            
            for rD, cD in directions:
                nR, nC = r+rD, c+cD
                if nR < 0 or nC < 0 or nR >= n or nC >= n or (nR, nC) in visited:
                    continue
                heapq.heappush(minH, [max(t, grid[nR][nC]), nR, nC])
                visited.add((nR,nC))
        return -1

            
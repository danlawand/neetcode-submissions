class Solution:
    def __init__(self):
        self.grid = None
        self.rows = None
        self.cols = None
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        if rows <= 0:
            return -1
        cols = len(grid[0])
        if cols <= 0:
            return -1
        
        self.grid = grid
        self.rows = rows
        self.cols = cols
        
        maxIslandArea = 0

        for row in range(rows):
            for col in range(cols):
                if self.grid[row][col] == 0:
                    continue
                maxIslandArea = max(maxIslandArea, self.calculateIslandArea(row, col))
        return maxIslandArea
        
    def calculateIslandArea(self, row, col) -> int:
        numberOfNodes = 0
        self.grid[row][col] = 0
        queue = deque([(row, col)])
        while queue:
            currRow, currCol = queue.pop()
            numberOfNodes += 1

            for verticalDirection, horizontalDirection in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                if currRow+verticalDirection < 0 or currRow+verticalDirection >= self.rows or currCol+horizontalDirection < 0 or currCol+horizontalDirection >= self.cols:
                    continue
                if self.grid[currRow+verticalDirection][currCol+horizontalDirection] == 0:
                    continue
                self.grid[currRow+verticalDirection][currCol+horizontalDirection] = 0
                queue.append((currRow+verticalDirection, currCol+horizontalDirection))

            # if currRow - 1 >= 0 and self.grid[currRow-1][currCol] == 1:
            #     self.grid[currRow-1][currCol] = 0
            #     queue.append((currRow-1, currCol))
            # if currRow + 1 < self.rows and self.grid[currRow+1][currCol] == 1:
            #     self.grid[currRow+1][currCol] = 0
            #     queue.append((currRow+1, currCol))
            # if currCol - 1 > 0 and self.grid[currRow][currCol-1] == 1:
            #     self.grid[currRow][currCol-1] = 0
            #     queue.append((currRow, currCol-1))
            # if currCol + 1 < self.cols and self.grid[currRow][currCol+1] == 1:
            #     self.grid[currRow][currCol+1] = 0
            #     queue.append((currRow, currCol+1))

        return numberOfNodes
class Solution:

    # Time O(n*m)
    # Memory O(n*m)
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        islands = 0
        def bfs(currI, currJ):
            grid[currI][currJ] = "0"
            queue.append((currI,currJ))
            while queue:
                currI, currJ = queue.popleft()
                if currI-1 >= 0:
                    if grid[currI-1][currJ] == "1":
                        queue.append((currI-1, currJ))
                        grid[currI-1][currJ] = "0"
                if currI+1 < rows:
                    if grid[currI+1][currJ] == "1":
                        queue.append((currI+1, currJ))
                        grid[currI+1][currJ] = "0"
                if currJ-1 >= 0:
                    if grid[currI][currJ-1] == "1":
                        queue.append((currI, currJ-1))
                        grid[currI][currJ-1] = "0"
                if currJ+1 < cols:
                    if grid[currI][currJ+1] == "1":
                        queue.append((currI, currJ+1))
                        grid[currI][currJ+1] = "0"

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    islands += 1
                    bfs(i, j)
        return islands
    
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        startRow = 0 
        endRow = n-1
        while startRow <= endRow:
            currRow = startRow + (endRow-startRow)//2
            if matrix[currRow][0] > target:
                endRow = currRow-1
                continue
            elif matrix[currRow][-1] < target:
                startRow = currRow+1
            else:
                startCol = 0
                endCol = m-1
                while startCol <= endCol:
                    currCol = startCol + (endCol-startCol)//2
                    if matrix[currRow][currCol] == target:
                        return True
                    elif matrix[currRow][currCol] > target:
                        endCol = currCol-1
                    else:
                        startCol = currCol+1
                return False
        return False
    
    def _searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            for number in row:
                if number == target:
                    return True
        return False
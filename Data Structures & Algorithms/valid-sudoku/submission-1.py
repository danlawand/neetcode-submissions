class Solution:

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowSets = [set() for _ in range(9)]
        colSets = [set() for _ in range(9)]
        boxSets = [[set(), set(), set()] for _ in range(3)]
        for i in range(len(board)):
            for j in range(len(board[0])):
                digit = board[i][j]
                if digit == ".":
                    continue
                if digit in boxSets[i//3][j//3] or digit in colSets[j] or digit in rowSets[i]:
                    return False
                
                colSets[j].add(digit)
                rowSets[i].add(digit)
                boxSets[i//3][j//3].add(digit)
        return True

    # O(81) --> O(n^2)
    # O(18) --> O(n)  auxiliary memory usage
    def _isValidSudoku(self, board: List[List[str]]) -> bool:
        # per row
        thereIsDigit = []
        for row in board:
            thereIsDigit = [False for _ in range(9)]
            for digit in row:
                if digit == ".":
                    continue
                if thereIsDigit[int(digit)-1]:
                    return False
                thereIsDigit[int(digit)-1] = True
        
        # per column
        nRows = len(board)
        nColumns = len(board[0]) # = 9
        for j in range(nColumns): # 9
            thereIsDigit = [False for _ in range(9)]
            for i in range(nRows):
                digit = board[i][j]
                if digit == ".":
                    continue
                if thereIsDigit[int(digit)-1]:
                    return False
                thereIsDigit[int(digit)-1] = True
            
        # per subbox
        # [1,1], [1,4], [1,7]
        # [4,1], [4,4], [4,7]
        # [7,1], [7,4], [7,7]
        # O(81)
        subBoxCenters = [[1,1], [1,4], [1,7],[4,1], [4,4], [4,7],[7,1], [7,4], [7,7]]
        positions = [[-1,-1],[-1,0],[-1,1], [0,-1],[0,0],[0,1],[1,-1],[1,0],[1,1]]
        for center in subBoxCenters: # 9 
            thereIsDigit = [False for _ in range(9)] # 9
            for i, j in positions: # 9
                i = i+center[0]
                j = j+center[1]
                digit = board[i][j] # 81
                if digit == ".":
                    continue
                if thereIsDigit[int(digit)-1]: # 
                    return False
                thereIsDigit[int(digit)-1] = True 
        return True



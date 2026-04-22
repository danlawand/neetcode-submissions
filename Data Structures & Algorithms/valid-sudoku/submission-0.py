class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
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
        for j in range(nColumns):
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
        subBoxCenters = [[1,1], [1,4], [1,7],[4,1], [4,4], [4,7],[7,1], [7,4], [7,7]]
        positions = [[-1,-1],[-1,0],[-1,1], [0,-1],[0,0],[0,1],[1,-1],[1,0],[1,1]]
        for center in subBoxCenters:
            thereIsDigit = [False for _ in range(9)]
            for i, j in positions:
                i = i+center[0]
                j = j+center[1]
                digit = board[i][j]
                if digit == ".":
                    continue
                if thereIsDigit[int(digit)-1]:
                    return False
                thereIsDigit[int(digit)-1] = True
        return True



from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [0]*9
        cols = [0]*9
        boxes = [[0]*3]*3
        for n in range(9):
            rows[n]=board[n]
            cols[n]=board[:][n]
            boxes[n//3][n%3] = rows[n][:3]
        print(cols)
        for row in rows:
            hash_row = {}
            for string in row:
                hash_row[string] = hash_row.get(string,0)+1
                if string != "." and hash_row[string] ==2:
                    return False
            hash_row.clear()
        for col in cols:
            hash_col = {}
            for string in col:
                hash_col[string] = hash_col.get(string,0)+1
                if string != "." and hash_col[string] ==2:
                    return False
            hash_col.clear()
        for box in boxes:
            hash_box = {}
            for row in box:
                for string in row:
                    hash_box[string] = hash_box.get(string,0)+1
                    if string != "." and hash_box[string] ==2:
                        return False
            hash_box.clear()
        return True
    
class Solution2:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        number = {"1","2","3","4","5","6","7","8","9"}
        for row in board:
            temp = number.copy()
            for num in row:
                print(row)
                if num != ".":
                    print(num)
                    if num not in temp:
                        return False
                    else:
                        temp.remove(num)               

        for n in range(9):
            col = []
            for m in range(9):
                col.append(board[m][n])
            print(col)
            temp = number.copy()
            for num in col:
                if num != ".":
                    if num not in temp:
                        return False
                    else:
                        temp.remove(num)      

        return True
        
    
solver = Solution2()
print(solver.isValidSudoku([["5","3",".",".","7",".",".",".","."],[ "6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]])) # True
print(solver.isValidSudoku([["8","3",".",".","7",".",".",".","."],[ "6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]])) # False
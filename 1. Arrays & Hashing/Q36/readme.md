# valid sudoku

## my answer1
~~~
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
~~~

### result
status: denied <br>
time: -- <br>
memory: -- <br>

## my answer2
~~~
class Solution:
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
~~~

### result
status: denied <br>
time: -- <br>
memory: -- <br>

## best solution1(semi-brute force, $` O(81) `$)
~~~
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)
        
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                
                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in boxes[(r // 3, c // 3)]:
                    return False
                
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                boxes[(r // 3, c // 3)].add(board[r][c])
        
        return True
~~~

## best solution2(using set, $` O(81) `$ )
~~~
class Solution2(object):
    def isValidSudoku(self, board):
        res = []
        for i in range(9):
            for j in range(9):
                element = board[i][j]
                print(element)
                if element != '.':
                    res += [(i, element), (element, j), (i // 3, j // 3, element)]
                    print(res)
        return len(res) == len(set(res))
~~~

## point
1\. think how to count up the contents efficiently. <br>
2\. .<br>

## good reference
1\. Nothing. <br>

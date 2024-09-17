from random import randrange
N = 9
def is_valid(sudoku): #check if sudoku is valid
    for i in range(9):
        if not is_valid_row(sudoku, i) or not is_valid_col(sudoku, i):
            return False
        if(i % 3 == 0):
            for j in range(0, 9, 3):
                if not is_valid_box(sudoku, i, j):
                    return False
    return True

def is_valid_row(sudoku, row):#check if row is valid
    nums = set()
    for i in range(9):
        if(sudoku[row][i] != 0 and sudoku[row][i]  in nums):
            return False
        nums.add(sudoku[row][i])
        
    return True

def is_valid_col(sudoku, col):#check if column is valid
    nums = set()
    for i in range(9):
        if(sudoku[i][col] != 0 and sudoku[i][col] in nums):
            return False
        nums.add(sudoku[i][col])
    return True

def is_valid_box(sudoku, i, j): # check if box is valid
    nums = set()
    for x in range(3):
        for y in range(3):
            if(sudoku[i + x][j + y] != 0 and sudoku[i + x][j + y] in nums):
                return False
            nums.add(sudoku[i + x][j + y])
    return True
def valid_num(row, col, num, sudoku): #returns True if num can be placed in (row, col) 
    if(not num):
        return True
    for i in range(9):
        if((sudoku[row][i] == num) or (sudoku[i][col] == num) or (sudoku[row-row % 3 + i // 3][col - col % 3 + i % 3] == num)):
            return False
    return True
def init_nums(grid, i, j):  # returns list of numbers that can be placed in (i, j)
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    used = set()
    for h in range(0, N):
        if(grid[i][h] != 0):
            used.add(grid[i][h])
    for h in range(0, N):
        if(grid[h][j] != 0):
            used.add(grid[h][j])
    istart = i - i % 3
    jstart = j - j % 3
    for h in range(istart, istart + 3):
        for k in range(jstart, jstart + 3):
            if(grid[h][k] != 0):
                used.add(grid[h][k])

    nums_copy = nums.copy()
    for num in nums_copy:
        if(num in used):
            #print(val)
            nums.remove(num)
    return nums

def gen_grid(m,n, grid):  # generates a complete sudoku
#    print(grid)
    if m == 9:
        return True
    nums = init_nums(grid, m, n)
    while(len(nums) > 0):
        i = randrange(0, len(nums))
        grid[m][n] = nums[i]
        nums.remove(nums[i])
        if(is_valid(grid)):
            if(n == 8):
                if(gen_grid(m+1,0, grid)):
                    return True
            elif(gen_grid(m,n+1,grid)):
                return True
        grid[m][n] = 0
    return False


def resolver2(sudoku, sols): # solves sudoku
    sol =[row[:] for row in sudoku] 
    def backtrack(sol, i, j):
        if(len(sols) == 2):
            return False
        if i == 9:
            sols.append([row[:] for row in sol])
            return True
        if sol[i][j] == 0:
            for k in range(1, 10):
                if(valid_num(i, j, k, sol)):
                    sol[i][j] = k
                    if(backtrack(sol, i + (j + 1) // 9, (j + 1) % 9) == False):
                        return False
                    sol[i][j] = 0
            return None
        else:
            if(backtrack(sol, i + (j + 1) // 9, (j + 1) % 9) == False):
                return False
            return None
    res = backtrack(sol, 0, 0)
    if(len(sols) == 1):
        return True
    if(len(sols) == 0):
        return None
    return False
    

def gen_scheme(grid): # generates a sudoku grid
    empty = 0
    for i in range(0, 9):
        for j in range(0, 9):
                to_delete = randrange(0, 2)
                if(to_delete):
                    val = grid[i][j]
                    grid[i][j] = 0
                    sols = []
                    if(not(resolver2(grid, sols) == True)):
                        grid[i][j] = val
                    else:
                        empty += 1
    return [grid, empty]
def gen_sudoku(): # generates sudoku
    sol = [[0 for i in range(9)] for j in range(9)]
    gen_grid(0, 0, sol)
    grid = [row[:] for row in sol]
    [grid, empty] = gen_scheme(grid)
    print(empty)
    return[grid, sol, empty]


N = 9
def test_sudoku(sudoku, empty_cells):#check if sudoku is valid, wether it's complete or not
    if(not empty_cells):
        for i in range(N):
            used_nums = set()
            for j in range(N):
                if(sudoku[i][j] in used_nums):
                    return 0
                else:
                    used_nums.add(sudoku[i][j])
        for j in range(N):
            used_nums = set()
            for i in range(N):
                if(sudoku[i][j] in used_nums):
                    return 0
                else:
                    used_nums.add(sudoku[i][j])
        for i in range(0, N, 3):
            for j in range(0, N, 3):
                used_nums = set()
                for h in range(i, i + 3):
                    for k in range(j , j + 3):
                        if(sudoku[h][k] in used_nums):
                            return 0
                        else:
                            used_nums.add(sudoku[h][k])
        return 1
    else:
        for i in range(N):
            used_nums = set()
            for j in range(N):
                if(sudoku[i][j] != 0):
                    if(sudoku[i][j] in used_nums):
                        return 0
                    else:
                        used_nums.add(sudoku[i][j])
        for j in range(N):
            used_nums = set()
            for i in range(N):
                if(sudoku[i][j] != 0):
                    if(sudoku[i][j] in used_nums):
                        return 0
                    else:
                        used_nums.add(sudoku[i][j])
        for i in range(0, N, 3):
            for j in range(0, N, 3):
                used_nums = set()
                for h in range(i, i + 3):
                    for k in range(j , j + 3):
                        if(sudoku[h][k] != 0):
                            if(sudoku[h][k] in used_nums):
                                return 0
                            else:
                                used_nums.add(sudoku[h][k])
        return -1
    

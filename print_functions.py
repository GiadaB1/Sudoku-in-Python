from pygame import*
from random import*
from resources import*

def print_error(i, j):#call in case of error, displays red rectangle
    incrementx = (j // 3) * 2.3
    draw.rect(screen, (255, 0, 0), Rect((XSTART+3.75 + j * (STEP+0.25)+incrementx), (YSTART+4 + i* (63)), 61,59.7))
def game_interface(sudoku, offset):#sudoku game interface
    screen.blit(sfondo, (0, 0))  
    screen.blit(grid, (grid_rect))
    screen.blit(check_btn, (check_btn_rect))
    screen.blit(solve_btn, (solve_btn_rect))
    screen.blit(back_arrow, (back_arrow_rect))
    screen.blit(info_btn, (info_btn_rect))
    screen.blit(new_sudoku_btn, (new_sudoku_btn_rect))
    display_timer(offset, 100, 30)
    current_cell(0, 0)
    display_mat(sudoku)

def free_box(i, j):
    incrementx = (j // 3) * 2.3
    draw.rect(screen, (255, 255, 255), Rect((XSTART+3.75 + j * (STEP+0.25)+incrementx), (YSTART+4 + i* (63)), 61,59.7))

def display_mat(mat): #displays matrix(sudoku) on screen
    for i in range(0, N):
        y = Y_N + i * STEP
        for j in range(0, N):
            if(mat[i][j] != 0):
                number = fontn.render(str(mat[i][j]), True, (0, 0, 0))
                screen.blit(number, ((X_N  + j * STEP), y))

def current_cell(i, j):#highlights current cell
    incrementx = (j // 3) * 2.3
    draw.rect(screen, (220, 220, 220), Rect((XSTART+3.75 + j * (STEP+0.25)+incrementx), (YSTART+4 + i* (63)), 61,59.7))

def print_value_of(mat, i, j, ncolor):#prints value of current cell
        offsetY = Y_N + i * STEP
        number = fontn.render(str(mat[i][j]), True, ncolor)
        screen.blit(number, ((X_N + j * STEP), offsetY))
def display_timer(start_time, x, y):#displays timer (hh:mm:ss)
        end_time = time.get_ticks()
        elapsed_time = end_time - start_time
        elapsed_time_s = (elapsed_time) // 1000
        h = elapsed_time_s // 3600
        mins = (elapsed_time_s % 3600) // 60
        sec = (elapsed_time_s % 3600) % 60
        text = font_timer.render(f"{h:02d}:{mins:02d}:{sec:02d}", True, (255, 255, 255))
        text_rect = text.get_rect(center=(x, y))
        screen.blit(text, text_rect)

def solver_interface():#sudoku solver interface
    screen.blit(sfondo, (0, 0))  
    screen.blit(grid, (grid_rect))
    screen.blit(solve_btn, (solve_btn_rect))
    screen.blit(back_arrow, (back_arrow_rect))
    screen.blit(info_btn, (info_btn_rect))
    screen.blit(clear_grid_btn, (clear_grid_btn_rect))
    current_cell(0, 0)

def print_errors(right_cells):#highlights all the errors in a sudoku with red rectangle
    for i in range(0, N):
        for j in range(0, N):
            if(right_cells[i][j] == 0):
                print_error(i, j)
def display_input(attempt, sudoku):#displays only the numbers entered by the user
    for i in range(0, N):
        for j in range(0, N):
            if(sudoku[i][j] == 0 and attempt[i][j] != 0):
                number = fontn.render(str(attempt[i][j]), True, attempt_numbers_col)
                screen.blit(number, ((X_N  + j * STEP), (Y_N + i* STEP)))
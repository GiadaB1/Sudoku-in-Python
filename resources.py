from pygame import*

init()
def update():
    display.update()
    time.Clock().tick(120)

screen = display.set_mode((0, 0), HWSURFACE)
screen_size = screen.get_size()
center = (screen_size[0] // 2, screen_size[1] // 2)

#FONTS

fontn = font.SysFont("Calibri", 60)
font_timer = font.SysFont("Calibri", 50)
font_info = font.SysFont("Calibri", 20)
titlefont = font.Font("media resources/OCRAEXT.ttf", 70)

#COLORS

ctitle = (230, 165, 249)
attempt_numbers_col = (21, 96, 130)

#IMAGES

play = image.load("media resources/play_btn.png")
quit = image.load("media resources/quit_btn.png")
puzzle_solver = image.load("media resources/puzzle_solver_btn.png")
sfondo = image.load("media resources/sfondo_partita.jpg") 
grid = image.load("media resources/grid.jpg")
solve_btn = image.load("media resources/solve_button_t.png")
back_arrow = image.load("media resources/back-arrow.png")
info_btn = image.load("media resources/info_button.png")
check_btn = image.load("media resources/check_button_t.png")
new_sudoku_btn = image.load("media resources/new_button.png")
clear_grid_btn = image.load("media resources/clear_grid_btn.png")
win_screen = image.load("media resources/win_screen.png")
play_again_btn = image.load("media resources/play_again_btn.png")
center = (screen_size[0] // 2, screen_size[1] // 2)
title = titlefont.render("Giada's Sudoku", True, ctitle)
title_rect = title.get_rect()
title_rect.center = (center[0], center[1] - 200)
play_btn_rect = play.get_rect()
play_btn_rect.center = (center[0], center[1])
quit_btn_rect = quit.get_rect()
quit_btn_rect.center = (center[0], center[1] + 200)
puzzle_solver_btn_rect = puzzle_solver.get_rect()
puzzle_solver_btn_rect.center = (center[0], center[1] + 100)
grid_rect = grid.get_rect()
grid_rect.center = (center[0], center[1])
solve_btn_rect = solve_btn.get_rect()
solve_btn_rect.center = (center[0] - 500, center[1])
back_arrow_rect = back_arrow.get_rect()
back_arrow_rect.bottomleft = (10, screen.get_height() - 10)
info_btn_rect = info_btn.get_rect()
info_btn_rect.topright = (screen.get_width() - 20, 20)
check_btn_rect = check_btn.get_rect()
check_btn_rect.center = (center[0] - 500, center[1] + 100)
new_sudoku_btn_rect = new_sudoku_btn.get_rect()
new_sudoku_btn_rect.center = (center[0] - 500, center[1] + 200)
clear_grid_btn_rect = clear_grid_btn.get_rect()
clear_grid_btn_rect.center = (center[0] - 500, center[1] + 100)
win_screen_rect = win_screen.get_rect()
win_screen_rect.center = (center[0], center[1])
play_again_btn_rect = play_again_btn.get_rect()
play_again_btn_rect.center = (center[0], center[1] + 300)

#COSTANT VALUES
N = 9
STEP = 63
XSTARTG = 100
YSTARTG = 200
XSTART = grid_rect.x
YSTART = grid_rect.y
X_N = XSTART + 20
Y_N = YSTART + 10
from pygame.locals import*
from algorithms import*
from input_tastiera import*
from test_sudoku import*
from print_functions import*
from math import*
from resources import*
#costanti
N = 9

init()
mixer.init()

def update_coords(ev, x, y): #returns the indices of the cell selected through the keyboard
    if(ev.key == K_LEFT and x > 0):
        x -= 1
    if(ev.key == K_RIGHT and x < 8):
        x += 1
    if(ev.key == K_UP and y > 0):
        y -= 1
    if(ev.key == K_DOWN and y < 8):
        y += 1
    return [x, y]


def on_info_btn(x, y, info_btn_rect): #returns True if the mouse is on the info button
    return sqrt((x - info_btn_rect.centerx)**2 + (y - info_btn_rect.centery)**2) <= (info_btn_rect.height / 2)
def menu():#displays the menu
    mixer.music.load("media resources/menu_music.mp3")
    mixer.music.play(-1)
    val = []
    for i in range(1, 20):
        val.append(randrange(1, 10))
    y_number = []
    for i in range(1, 20):
        y_number.append(randrange(-1000, 0))
    x_number = []
    x_number.append(0)
    for i in range(1, 19):
        x_number.append(x_number[i - 1] + 100)
    running = True
    while running:
        screen.blit(sfondo, (0, 0))
        for i in range(0, 19):
            if(y_number[i] <= 900):
                y_number[i] += 3
                number = fontn.render(str(val[i]), True, attempt_numbers_col)
                screen.blit(number, (x_number[i],y_number[i]))
            else:
                y_number[i] = randrange(-50, 0)
                val[i] = randrange(1, 10)
        for ev in event.get():
            x, y = mouse.get_pos()
            if ev.type == QUIT:
                running = False
            if(ev.type == MOUSEBUTTONDOWN):
                if(play_btn_rect.collidepoint(x,y)):
                    mixer.music.stop()
                    return "game"
                elif (quit_btn_rect.collidepoint(x, y)):
                    running = False
                elif(puzzle_solver_btn_rect.collidepoint(x, y)):
                    return "solver"
        screen.blit(title, title_rect)
        screen.blit(play, play_btn_rect)
        screen.blit(puzzle_solver, puzzle_solver_btn_rect)
        screen.blit(quit, quit_btn_rect)
        update()
def game():#sudoku game: displays sudoku to be solved 
    mixer.music.load("media resources/game_music.mp3")
    mixer.music.play(-1)
    prev_loop_time = time.get_ticks() #time spent in the previous loop
    [sudoku, solution, empty] = gen_sudoku()
    attempt = [row[:] for row in sudoku] 
    game_interface(sudoku, prev_loop_time)
    screen_size = screen.get_size()
    cc_x = 0
    cc_y = 0 #current cell indexes
    res = 2
    start_display_msg = 0
    current_pos = False
    running = True
    while running:
        draw.rect(screen, (14, 121, 167), (10, 10, 178, 40))
        display_timer(prev_loop_time, 100, 30)
        if((res == 0 or res ==-1) and time.get_ticks() - start_display_msg >= 3000):
            game_interface(sudoku, prev_loop_time)
            display_input(attempt, sudoku)
            cc_x = 0
            cc_y = 0
            res = 2
        for ev in event.get():
            x, y = mouse.get_pos()
            if ev.type == QUIT:
                running = False
            if(ev.type == KEYDOWN):
                if(attempt[cc_y][cc_x] == 0):
                    value = numbers(ev)
                    if(value):
                        attempt[cc_y][cc_x] = value
                        empty -= 1
                        print_value_of(attempt, cc_y, cc_x, attempt_numbers_col)
                elif(sudoku[cc_y][cc_x] == 0):
                    if(ev.key == K_BACKSPACE):
                        attempt[cc_y][cc_x] = 0
                        empty += 1
                free_box(cc_y, cc_x)  
                if(sudoku[cc_y][cc_x] != 0):
                    print_value_of(sudoku, cc_y, cc_x, (0, 0, 0))
                elif(attempt[cc_y][cc_x] != 0):
                    print_value_of(attempt, cc_y, cc_x, attempt_numbers_col)       
                [cc_x, cc_y] = update_coords(ev, cc_x, cc_y)
                current_cell(cc_y, cc_x)
                if(sudoku[cc_y][cc_x] != 0):
                    print_value_of(sudoku, cc_y, cc_x, (0, 0, 0))
                elif(attempt[cc_y][cc_x] != 0):
                    print_value_of(attempt, cc_y, cc_x, attempt_numbers_col)
            if(ev.type == MOUSEBUTTONDOWN):
                if(solve_btn_rect.collidepoint(x, y)):
                    for i in range(0, N):
                        for j in range(0, N):
                            free_box(i, j)
                    sudoku = [row[:] for row in solution]
                    display_mat(solution)
                elif(new_sudoku_btn_rect.collidepoint(x, y)):
                    return "game"        
                elif(check_btn_rect.collidepoint(x, y)):
                    res = test_sudoku(attempt, empty)
                    if(res == 1):
                        return "win"
                    elif(res == 0):
                        mixer.Sound("media resources/wrong_way.wav").play()
                        msg = font_timer.render("Something ain't right!", True, (0, 0, 0))
                        rect_msg = msg.get_rect()
                        rect_msg.center = screen.get_rect().center
                        screen.blit(msg, (rect_msg.x, rect_msg.y - 350))
                        start_display_msg = time.get_ticks()
                    else:
                        start_display_msg = time.get_ticks()
                        mixer.Sound("media resources/right_way.wav").play()
                        msg = font_timer.render("Keep on going, never give up!", True, (0, 0, 0))
                        rect_msg = msg.get_rect()
                        rect_msg.center = screen.get_rect().center
                        screen.blit(msg, (rect_msg.x, rect_msg.y - 350))
                elif(back_arrow_rect.collidepoint(x, y)):
                    return "menu"
            previous_pos = current_pos
            current_pos = on_info_btn(x, y, info_btn_rect)
            if(previous_pos == False and current_pos):          
                text = """move on the sudoku sudoku using arrows\npress 'Backspace' to erase a number\nclick on the 'solve' button to solve the puzzle\nclick on the 'Generate new sudoku' button to start a new puzzle\nclick on the 'Quit' button to exit the game\nclick on the 'Check solution' button to check your solution"""
                lines = text.split("\n")
                for i,line in enumerate(lines):
                    msg = font_info.render(line, True, (0, 0, 0))
                    screen.blit(msg, (center[0] + 50, center[1] - 450 + i*25))
            elif(current_pos == False and previous_pos):
                game_interface(sudoku, prev_loop_time)
                display_input(attempt, sudoku)
                cc_x = 0
                cc_y = 0
        update()
    
def sudoku_solver():#interface for solving sudoku
    solver_interface()
    running = True
    sudoku = [[0 for i in range(N)] for j in range(N)]
    right_cells = [[1 for i in range(N)] for j in range(N)]
    cc_y, cc_x = 0, 0
    mixer.music.load("media resources/game_music.mp3")
    mixer.music.play(-1)
    current_pos = False
    timer_running = False
    while running:
        for ev in event.get():
            x, y = mouse.get_pos()
            current_time = time.get_ticks()
            if(timer_running and current_time - start_timer > 3000):
                timer_running = False
                start_timer = 0
                solver_interface()
                print_errors(right_cells)
                current_cell(0,0)
                display_mat(sudoku)
                cc_x = 0
                cc_y = 0
            if(ev.type == KEYDOWN):
                value = numbers(ev)
                if(value != 0 and sudoku[cc_y][cc_x] == 0):
                    right_cells[cc_y][cc_x] = valid_num(cc_y, cc_x, value, sudoku)
                    sudoku[cc_y][cc_x] = value
                    print_value_of(sudoku, cc_y, cc_x, (0, 0, 0))
                else:
                    if(ev.key == K_BACKSPACE):
                        sudoku[cc_y][cc_x] = 0
                        right_cells[cc_y][cc_x] = 1
                        current_cell(cc_y, cc_x)
                    else:
                        if(right_cells[cc_y][cc_x]):
                            free_box(cc_y, cc_x)
                        else:
                            print_error(cc_y, cc_x)
                        if(sudoku[cc_y][cc_x] != 0):
                            print_value_of(sudoku, cc_y, cc_x, (0, 0, 0))       
                        [cc_x, cc_y] = update_coords(ev, cc_x, cc_y)
                        current_cell(cc_y, cc_x)
                        if(sudoku[cc_y][cc_x] != 0):
                            print_value_of(sudoku, cc_y, cc_x, (0, 0, 0))
            if(ev.type == MOUSEBUTTONDOWN):
                if(solve_btn_rect.collidepoint(x, y)):
                    sol = []
                    if(is_valid(sudoku)):
                        if(resolver2(sudoku, sol)):
                            display_mat(sol[0])
                            msg = font_timer.render("Sudoku solved!", True, (0, 0, 0))
                            msg_rect = msg.get_rect()
                            msg_rect.center = (center[0], center[1])
                            screen.blit(msg, msg_rect)
                        else:
                            msg = font_timer.render("Sudoku unsolvable!", True, (0, 0, 0))
                            screen.blit(msg, (center[0], center[1] - 400))
                            time.set_timer(USEREVENT, 3000)
                            timer_running = True
                            start_timer = time.get_ticks()
                    else:
                        msg = font_timer.render("Not valid!", True, (0, 0, 0))
                        screen.blit(msg, (center[0], center[1] - 400))
                        time.set_timer(USEREVENT, 3000)
                        timer_running = True
                        start_timer = time.get_ticks()                
                elif(back_arrow_rect.collidepoint(x, y)):
                    return "menu"
                elif(clear_grid_btn_rect.collidepoint(x, y)):
                    return "solver"
            elif(ev.type == QUIT):
                running = False
            previous_pos = current_pos
            current_pos = on_info_btn(x, y, info_btn_rect)
            if(previous_pos == False and current_pos):          
                text = """move on the sudoku sudoku using arrows\npress 'Backspace' to erase a number\nclick on the 'solve' button to solve the puzzle\nclick on the 'Generate new sudoku' button to start a new puzzle\nclick on the 'Quit' button to exit the game\nclick on the 'Check solution' button to check your solution"""
                lines = text.split("\n")
                for i,line in enumerate(lines):
                    msg = font_info.render(line, True, (0, 0, 0))
                    screen.blit(msg, (center[0] + 50, center[1] - 450 + i*25))
            elif(current_pos == False and previous_pos):
                solver_interface()
                print_errors(right_cells)
                display_mat(sudoku)
                cc_x = 0
                cc_y = 0
        update()
def display_win_screen(prev_loop_time):#displays victory screen
    mixer.Sound("media resources/victory_music.wav").play()
    overlay = Surface((screen_size[0], screen_size[1]))
    overlay.fill((0, 0, 0))
    overlay.set_alpha(160) 
    screen.blit(overlay, (0, 0))
    screen.blit(win_screen, (win_screen_rect))
    screen.blit(play_again_btn, (play_again_btn_rect))
    screen.blit(back_arrow, (back_arrow_rect))
    display_timer(prev_loop_time, center[0], center[1] + 100)
    while True:
        for ev in event.get():
            x,y = mouse.get_pos()
            if ev.type == QUIT:
                return False
            if ev.type == MOUSEBUTTONDOWN:
                if(back_arrow_rect.collidepoint(x,y)):
                    return "menu"
                elif(play_again_btn_rect.collidepoint(x,y)):
                    return "game"
        update()


#main loop
running = True
mode = "menu"
prev_loop_time = 0
while(running):
    if(mode == "menu"):
        mode = menu()
    elif(mode == "game"):
        start_loop_time = time.get_ticks()
        mode = game()
    elif(mode == "win"):
        mode = display_win_screen(start_loop_time)
    elif(mode == "solver"):
       mode = sudoku_solver()
    else:
        running = False
    mixer.stop()
import curses

def screen(stdscr):
    stdscr.clear()
    x_start_pos = 1
    cur_x    = 1
    cur_y    = 1
    k        = 0
    sort_int = 0
    black    = curses.COLOR_BLACK
    cyan     = curses.COLOR_CYAN
    red      = curses.COLOR_RED
    white    = curses.COLOR_WHITE
    green    = curses.COLOR_GREEN
    curses.start_color()
    curses.init_pair(1, cyan, black)
    curses.init_pair(2, red, black)
    curses.init_pair(3, black, white)
    curses.init_pair(4, green, black)
    
if __name__ == "__main__":
    print("Hello World!")
    #this is where we will link to the game start as soon as it's operational. 


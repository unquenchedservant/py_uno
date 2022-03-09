import curses
import logging
import os
import sys
from utilities import menu as m

def screen(stdscr):
    curses.start_color()
    black    = curses.COLOR_BLACK
    cyan     = curses.COLOR_CYAN
    red      = curses.COLOR_RED
    white    = curses.COLOR_WHITE
    green    = curses.COLOR_GREEN
    curses.init_pair(1, cyan, black)
    curses.init_pair(2, red, black)
    curses.init_pair(3, black, white)
    curses.init_pair(4, green, black)
    
    stdscr.clear()
    x_start_pos = 1
    cur_x    = 1
    cur_y    = 1
    k        = 0
    curses.curs_set(0)
    stdscr.clear()
    stdscr.refresh()
    
    profile_path = os.getcwd() + "profile/"
    title_str = "Uno Game v0.0.1a"
    status_msg = "Written by Jonathan Thorne | © 2022 | Use arrow keys to navigate || Press esc to quit"
    option_1  = "1. Play Quick Game (Working)" #Quick, semi-traditional, gameplay. no scores. 
    option_2   = "2. Play Full Game (Coming soon)"  #full game, full rules. 
    option_3   = "3. Statistics (Coming soon)" #will contain option to delete profile in here.
    option_4   = "4. Exit" 
    stdscr.clear()
    while(True):
        m.title(stdscr, title_str)
        m.status_bar(stdscr, status_msg)
        m.menu_option(stdscr, option_1, 1, 1, cur_y) #TODO menu_option function
        m.menu_option(stdscr, option_2, 2, 1, cur_y)
        m.menu_option(stdscr, option_3, 3, 1, cur_y)
        m.menu_option(stdscr, option_4, 4, 1, cur_y)
        stdscr.refresh()
        k = stdscr.getch()
        if k == 27 or k == ord('q'):
            sys.exit()
        
        if k == curses.KEY_UP:
            cur_y -= 1
            if cur_y == 0:
                cur_y = 4
        elif k == curses.KEY_DOWN:
            cur_y += 1
            if cur_y == 5:
                cur_y = 1
        elif k == 10 or k == curses.KEY_RIGHT:
            if cur_y == 1:
                logging.warning("Play quick game")
                sys.exit()
            elif cur_y == 2:
                logging.warning("play full game")
                sys.exit()
            elif cur_y == 3:
                logging.warning("statistics")
                sys.exit()
            elif cur_y == 4:
                sys.exit()
        elif k == ord('1'):
            logging.warning("play quick game")
            sys.exit()
        elif k == ord('2'):
            logging.warning("play full game")
            sys.exit()
        elif k == ord('3'):
            logging.warning("statistics")
            sys.exit()
        elif k == ord('4'):
            sys.exit()

def start():
    curses.wrapper(screen)


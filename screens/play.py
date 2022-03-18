import curses
import os
from utilities import menu as m
import sys
from screens import main
import logging

def screen(stdscr, fullGame):
    stdscr.clear()
    x_start_pos = 1
    cur_x    = 1
    cur_y    = 1
    k        = 0
    curses.curs_set(0)
    stdscr.clear()
    stdscr.refresh()
    
    profile_path = os.getcwd() + "profile/"
    gameVersionStr = ""
    if fullGame:
        gameVersionStr = " (Full Game)" 
    else:
        gameVersionStr = " (Quick Game)"

    title_str = "How many computers?" + gameVersionStr
    status_msg = "Written by Jonathan Thorne | © 2022 | Use arrow keys to navigate || Press esc to quit"
    option_1  = "1" #1 Computer
    option_2   = "2"  #2 Computers
    option_3   = "3" #3 Computers
    option_4   = "Back To Main Menu" #back to the main Menu
    stdscr.clear()
    while(True):
        m.title(stdscr, title_str)
        m.status_bar(stdscr, status_msg)
        m.menu_option(stdscr, option_1, 1, 1, cur_y)
        m.menu_option(stdscr, option_2, 2, 1, cur_y)
        m.menu_option(stdscr, option_3, 3, 1, cur_y)
        m.menu_option(stdscr, option_4, 4, 1, cur_y)
        stdscr.refresh()
        k = stdscr.getch()
        if k == ord('q'):
            sys.exit()
        elif k == 27:
            main.start()
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
                logging.warning("1 Computer")
                sys.exit()
            elif cur_y == 2:
                logging.warning("2 Computer")
                sys.exit()
            elif cur_y == 3:
                logging.warning("3 Computer")
                sys.exit()
            elif cur_y == 4:
                main.start()
        elif k == ord('1'):
            logging.warning("1 Computer")
            sys.exit()
        elif k == ord('2'):
            logging.warning("2 Computer")
            sys.exit()
        elif k == ord('3'):
            logging.warning("3 Computer")
            sys.exit()
        elif k == ord('4'):
            main.start()

def start(fullGame=False):
    curses.wrapper(screen, fullGame)
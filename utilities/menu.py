import curses
from utilities import arithmetic
bold   = curses.A_BOLD

def get_height(stdscr):
    return stdscr.getmaxyx()[0]
def get_width(stdscr):
    return stdscr.getmaxyx()[1]
def title(stdscr, title):
    display_x = arithmetic.title_start(title, get_width(stdscr))
    stdscr.attron(curses.color_pair(1))
    stdscr.attron(bold)
    stdscr.addstr(0, display_x, title)
    stdscr.attroff(bold)
    stdscr.attroff(curses.color_pair(1))
def status_bar(stdscr, msg):
    height = get_height(stdscr)
    width  = get_width(stdscr)
    display_y = height - 1
    magic_number = (width - len(msg) - 1)
    stdscr.attron(curses.color_pair(3))
    stdscr.addstr(display_y, 0, msg)
    stdscr.addstr(display_y, len(msg), " " * magic_number)
    stdscr.attroff(curses.color_pair(3))
def menu_option(stdscr, string, display_y, display_x, cursor_y):
    if cursor_y == display_y:
        stdscr.attron(curses.color_pair(3))
    stdscr.addstr(display_y, display_x, string)
    if cursor_y == display_y:
        stdscr.attroff(curses.color_pair(3))
import curses
from utilities import arithmetic, menuhelpers

color1 = curses.color_pair(1)
color2 = curses.color_pair(2)
color3 = curses.color_pair(3)
color4 = curses.color_pair(4)
bold   = curses.A_BOLD

def get_height(stdscr):
    return stdscr.getmaxyx()[0]
def get_width(stdscr):
    return stdscr.getmaxyx()[1]
def title(stdscr, title):
    display_x = arithmetic.title_start(title, get_width(stdscr))
    stdscr.attron(color1)
    stdscr.attron(bold)
    stdscr.addstr(0, display_x, title)
    stdscr.attroff(bold)
    stdscr.attroff(color1)
def status_bar(stdscr, msg):
    height = get_height(stdscr)
    width  = get_width(stdscr)
    display_y = height - 1
    magic_number = (width - len(msg) - 1)
    stdscr.attron(color3)
    stdscr.addstr(display_y, 0, msg)
    stdscr.addstr(display_y, len(msg), " " * magic_number)

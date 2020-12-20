"""
MIT License
#
# Copyright (c) 2020 Ferhat Geçdoğan All Rights Reserved.
# Distributed under the terms of the MIT License.
#
#
"""

"""
	Maybe use lambda from __future__ 
"""

# from __future__ import print_function

ESC = 0o33

# Default Background color definitions
DEFAULT = 39
BLACK = 30
RED = 31
GREEN = 32
YELLOW = 33
BLUE = 34
MAGENTA = 35
CYAN = 36
WHITE = 37
LIGHT_BLACK = 90
LIGHT_RED = 91
LIGHT_GREEN = 92
LIGHT_YELLOW = 93
LIGHT_BLUE = 94
LIGHT_MAGENTA = 95
LIGHT_CYAN = 96
LIGHT_WHITE = 97

# Default Foreground Color Definitions
FDEFAULT = 49
FBLACK = 40
FRED = 41
FGREEN = 42
FYELLOW = 43
FBLUE = 44
FMAGENTA = 45
FCYAN = 46
FLIGHT_GRAY = 47
FDARK_GRAY = 100
FLIGHT_RED = 101
FLIGHT_GREEN = 102
FLIGHT_YELLOW = 103
FLIGHT_BLUE = 104
FLIGHT_MAGENTA = 105
FLIGHT_CYAN = 106
FWHITE = 107   

# Default Set Type Definitions
SDEFAULT = 0
BOLD = 1
DIM = 2
UNDERLINED = 4
BLINK = 5
REVERSE = 7
HIDDEN = 8

# Default Unset Type Definitions  
UALL = 0
UBOLD = 21
UDIM = 22
UUNDERLINED = 24
UBLINK = 25
UREVERSE = 27
UHIDDEN = 28

DEFAULT = 39
BLACK = 30
RED = 31
GREEN = 32
YELLOW = 33
BLUE = 34
MAGENTA = 35
CYAN = 36
WHITE = 37
LIGHT_BLACK = 90
LIGHT_RED = 91
LIGHT_GREEN = 92
LIGHT_YELLOW = 93
LIGHT_BLUE = 94
LIGHT_MAGENTA = 95
LIGHT_CYAN = 96
LIGHT_WHITE = 97

# Pre-defined colors.
def RED_COLOR(): 
	print("\033[0;31m");
	
def GREEN_COLOR(): 
	print("\033[0;32m");

def YELLOW_COLOR():
	print("\033[0;33m");

def BLUE_COLOR():
	print("\033[0;34m");

def MAGENTA_COLOR():
	print("\033[0;35m");
	
def CYAN_COLOR():
	print("\033[0;36m");

def LIGHT_BLACK_COLOR():
	print("\033[0;90m");
	
def LIGHT_RED_COLOR():
	print("\033[0;91m");

def LIGHT_GREEN_COLOR():
	print("\033[0;92m");

def LIGHT_YELLOW_COLOR():
	print("\033[0;93m");

def LIGHT_BLUE_COLOR():
	print("\033[0;94m");

def LIGHT_MAGENTA_COLOR():
	print("\033[0;95m");

def LIGHT_CYAN_COLOR():
	print("\033[0;96m");

def LIGHT_WHITE_COLOR():
	print("\033[0;97m");

# Default bold** color definitions
def BOLD_RED_COLOR():
	print("\033[1;31m");

def BOLD_GREEN_COLOR():
	print("\033[1;32m");

def BOLD_YELLOW_COLOR():
	print("\033[01;33m");

def BOLD_BLUE_COLOR():
	print("\033[1;34m");

def BOLD_MAGENTA_COLOR():
	print("\033[1;35m");
	
def BOLD_CYAN_COLOR(): 
	print("\033[1;36m");
def BOLD_LIGHT_BLACK_COLOR():
	print("\033[1;90m");
	
def BOLD_LIGHT_RED_COLOR(): 
	print("\033[1;91m");

def BOLD_LIGHT_GREEN_COLOR(): 
	print("\033[1;92m");

def BOLD_LIGHT_YELLOW_COLOR():
	print("\033[1;93m");

def BOLD_LIGHT_BLUE_COLOR():
	print("\033[1;94m");

def BOLD_LIGHT_MAGENTA_COLOR():
	print("\033[1;95m");

def BOLD_LIGHT_CYAN_COLOR():
	print("\033[1;96m");

def BOLD_LIGHT_WHITE_COLOR():
	print("\033[1;97m");

# Reset (BLACK)
def BLACK_COLOR():
	print("\033[0m");

def WHITE_COLOR():
	print("\033[1;37m");

# Default color definitions without printlnf
WRED_COLOR = "\033[0;31m"
WGREEN_COLOR = "\033[0;32m"
WYELLOW_COLOR = "\033[0;33m"
WBLUE_COLOR = "\033[0;34m"
WMAGENTA_COLOR = "\033[0;35m"
WCYAN_COLOR = "\033[0;36m"
WLIGHT_BLACK_COLOR = "\033[0;90m"
WLIGHT_RED_COLOR = "\033[0;91m"
WLIGHT_GREEN_COLOR = "\033[0;92m"
WLIGHT_YELLOW_COLOR = "\033[0;93m"
WLIGHT_BLUE_COLOR = "\033[0;94m"
WLIGHT_MAGENTA_COLOR = "\033[0;95m"
WLIGHT_CYAN_COLOR = "\033[0;96m"
WLIGHT_WHITE_COLOR = "\033[0;97m"

# Default bold** color definitions without printlnf
WBOLD_RED_COLOR = "\033[1;31m"
WBOLD_GREEN_COLOR = "\033[1;32m"
WBOLD_YELLOW_COLOR = "\033[01;33m"
WBOLD_BLUE_COLOR = "\033[1;34m"
WBOLD_MAGENTA_COLOR = "\033[1;35m"
WBOLD_CYAN_COLOR = "\033[1;36m"
WBOLD_LIGHT_BLACK_COLOR = "\033[1;90m"
WBOLD_LIGHT_RED_COLOR = "\033[1;91m"
WBOLD_LIGHT_GREEN_COLOR = "\033[1;92m"
WBOLD_LIGHT_YELLOW_COLOR = "\033[1;93m"
WBOLD_LIGHT_BLUE_COLOR = "\033[1;94m"
WBOLD_LIGHT_MAGENTA_COLOR = "\033[1;95m"
WBOLD_LIGHT_CYAN_COLOR = "\033[1;96m"
WBOLD_LIGHT_WHITE_COLOR = "\033[1;97m"

WBOLD_WHITE_COLOR = "\033[1;37m"

# Sign
Semicolon = ";"
Mark = "m"
Template = "\033["

# Reset (BLACK)
WBLACK_COLOR = "\033[0m"

# Foreground 
def TextBackground(color):
    print("%c[%dm" + ESC + 40+color)

# PrintWith(Colorize(type, color), "text")
def PrintWith(color, text):
    print(color + text + WBLACK_COLOR, end = '')

# Colorize without Reset (WBLACK_COLOR)
def PrintWhReset(color, text):
    print(color + text, end = '')

# Colorize
def Colorize(type, color):
    return str(Template + str(type) + Semicolon + str(color) + Mark)

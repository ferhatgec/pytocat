# MIT License
#
# Copyright (c) 2020 Ferhat Geçdoğan All Rights Reserved.
# Distributed under the terms of the MIT License.
#
#

from lib.colorized import *

def centerText(text, language):
    print("🔒 " + WBOLD_LIGHT_MAGENTA_COLOR + text + WBLACK_COLOR, end='')
    print(WBOLD_LIGHT_BLUE_COLOR + " │" + WBOLD_LIGHT_RED_COLOR + " " + language + "\n ", end='')
    
def print_top_header(length: int = 10):
    BOLD_YELLOW_COLOR()
    
    # print top-left corner
    print("  ╭", end='')
    
    i = 0
    
    while i != length:
        print("───", end='')
        i += 1
    
    # print top-right corner    
    print("╮\n " + " │ " + WBLACK_COLOR, end='') 
    
    BLACK_COLOR()

def print_bottom_header(length: int = 10):
    BOLD_LIGHT_CYAN_COLOR()
    
    # print top-left corner
    print(" ╰", end='')
    
    i = 0
    
    while i != length:
        print("───", end='')
        i += 1
    
    # print top-right corner
    print("╯") 
    BLACK_COLOR()


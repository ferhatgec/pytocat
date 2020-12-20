# MIT License
#
# Copyright (c) 2020 Ferhat Geçdoğan All Rights Reserved.
# Distributed under the terms of the MIT License.
#
#

import sys
import os

import languages
import header

from lib.colorized import *

version = "0.1"

def SetHeader(filename):
    extension = os.path.splitext(filename)
    
    header.print_top_header(10)
    
    if extension[1] == ".cpp":
        header.centerText(filename, "C++")
    else:
        header.centerText(filename, "Regular")
    
    header.print_bottom_header(10)
    
def ReadFile(filename):
    file = open(filename, 'r') 
    lines = file.readlines() 
    extension = os.path.splitext(filename)
    
    if extension[1] == ".cpp":
        for line in lines: 
            languages.CPlusPlus(line)
    else:
        for line in lines: 
            languages.Regular(line)
	
def HelpFunction(argument):
    PrintWith(Colorize(BOLD, RED), "Fegeya ")
    PrintWith(Colorize(BOLD, GREEN), "PytoCat ")
    PrintWith(Colorize(BOLD, BLUE), version)
    PrintWith(Colorize(BOLD, YELLOW), "\nColorized 'cat' implementation.\n")
    PrintWith(Colorize(BOLD, LIGHT_MAGENTA), argument + " [file]\n")
    
if len(sys.argv) < 2:
    HelpFunction(sys.argv[0])
    sys.exit(1)
else:
    SetHeader(sys.argv[1])
    ReadFile(sys.argv[1])

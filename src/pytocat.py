# MIT License
#
# Copyright (c) 2020 Ferhat Geçdoğan All Rights Reserved.
# Distributed under the terms of the MIT License.
#
#

import sys
import os
import languages

from lib.colorized import *

version = "0.1"

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
    ReadFile(sys.argv[1])

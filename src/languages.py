# MIT License
#
# Copyright (c) 2020 Ferhat Geçdoğan All Rights Reserved.
# Distributed under the terms of the MIT License.
#
#

from lib.colorized import *   

def CPlusPlus(line):
    line = line.replace("int", WBOLD_BLUE_COLOR + "int" + WBLACK_COLOR)

    line = line.replace("long", WBOLD_BLUE_COLOR + "long" + WBLACK_COLOR)
    
    line = line.replace("bool", WBOLD_BLUE_COLOR + "bool" + WBLACK_COLOR)
    line = line.replace("char", WBOLD_BLUE_COLOR + "char" + WBLACK_COLOR)
    line = line.replace("auto", WBOLD_BLUE_COLOR + "auto" + WBLACK_COLOR)
    
    line = line.replace("if", WBOLD_LIGHT_RED_COLOR + "if" + WBLACK_COLOR)
    line = line.replace("else", WBOLD_LIGHT_RED_COLOR + "else" + WBLACK_COLOR)
    
    line = line.replace("for", WBOLD_MAGENTA_COLOR + "for" + WBLACK_COLOR)
    line = line.replace("do", WBOLD_MAGENTA_COLOR + "do" + WBLACK_COLOR)
    line = line.replace("while", WBOLD_MAGENTA_COLOR + "while" + WBLACK_COLOR)
    
    line = line.replace("void", WBOLD_RED_COLOR + "void" + WBLACK_COLOR)
    line = line.replace("main", WBOLD_LIGHT_RED_COLOR + "main" + WBLACK_COLOR)
    line = line.replace("asm", WBOLD_LIGHT_RED_COLOR + "asm" + WBLACK_COLOR)
    
    line = line.replace("const", WBOLD_LIGHT_BLUE_COLOR + "const" + WBLACK_COLOR)
    line = line.replace("static", WBOLD_LIGHT_BLUE_COLOR + "static" + WBLACK_COLOR)
    line = line.replace("extern", WBOLD_LIGHT_BLUE_COLOR + "extern" + WBLACK_COLOR)
    line = line.replace("inline", WBOLD_LIGHT_BLUE_COLOR + "inline" + WBLACK_COLOR)
    line = line.replace("virtual", WBOLD_LIGHT_BLUE_COLOR + "virtual" + WBLACK_COLOR)
    line = line.replace("friend", WBOLD_LIGHT_BLUE_COLOR + "friend" + WBLACK_COLOR)
    
    line = line.replace("public", WBOLD_LIGHT_BLUE_COLOR + "public" + WBLACK_COLOR)
    line = line.replace("private", WBOLD_LIGHT_BLUE_COLOR + "private" + WBLACK_COLOR)
    line = line.replace("protected", WBOLD_LIGHT_BLUE_COLOR + "protected" + WBLACK_COLOR)

    line = line.replace("#include", WBOLD_YELLOW_COLOR + "#include" + WBLACK_COLOR)
    
    line = line.replace("typedef", WBOLD_MAGENTA_COLOR + "typedef" + WBLACK_COLOR)
    
    line = line.replace("#define", WBOLD_MAGENTA_COLOR + "#define" + WBLACK_COLOR)
    line = line.replace("#ifndef", WBOLD_MAGENTA_COLOR + "#ifndef" + WBLACK_COLOR)
    line = line.replace("#ifdef", WBOLD_MAGENTA_COLOR + "#ifdef" + WBLACK_COLOR)
    line = line.replace("#endif", WBOLD_MAGENTA_COLOR + "#endif" + WBLACK_COLOR)
    
    line = line.replace("return", WBOLD_LIGHT_MAGENTA_COLOR + "return" + WBLACK_COLOR)
    
    line = line.replace("nodiscard", WBOLD_MAGENTA_COLOR + "nodiscard" + WBLACK_COLOR)

    line = line.replace("class", WBOLD_LIGHT_YELLOW_COLOR + "class" + WBLACK_COLOR)
    line = line.replace("struct", WBOLD_LIGHT_YELLOW_COLOR + "struct" + WBLACK_COLOR)
    line = line.replace("namespace", WBOLD_LIGHT_YELLOW_COLOR + "namespace" + WBLACK_COLOR)
    
    line = line.replace("using", WBOLD_GREEN_COLOR + "using" + WBLACK_COLOR)
    
    line = line.replace("std", WBOLD_LIGHT_YELLOW_COLOR + "std" + WBLACK_COLOR)
    
    line = line.replace("iostream", WBOLD_LIGHT_MAGENTA_COLOR + "iostream" + WBLACK_COLOR)
    line = line.replace("cstring", WBOLD_LIGHT_MAGENTA_COLOR + "cstring" + WBLACK_COLOR)
    line = line.replace("sstream", WBOLD_LIGHT_MAGENTA_COLOR + "sstream" + WBLACK_COLOR)
    line = line.replace("fstream", WBOLD_LIGHT_MAGENTA_COLOR + "fstream" + WBLACK_COLOR)
    line = line.replace("memory", WBOLD_LIGHT_MAGENTA_COLOR + "memory" + WBLACK_COLOR)
    line = line.replace("cstdlib", WBOLD_LIGHT_MAGENTA_COLOR + "cstdlib" + WBLACK_COLOR)
    line = line.replace("cstdio", WBOLD_LIGHT_MAGENTA_COLOR + "cstdio" + WBLACK_COLOR)
    line = line.replace("vector", WBOLD_LIGHT_MAGENTA_COLOR + "vector" + WBLACK_COLOR)
    line = line.replace("algorithm", WBOLD_LIGHT_MAGENTA_COLOR + "algorithm" + WBLACK_COLOR)
    line = line.replace("thread", WBOLD_LIGHT_MAGENTA_COLOR + "thread" + WBLACK_COLOR)
    line = line.replace("array", WBOLD_LIGHT_MAGENTA_COLOR + "array" + WBLACK_COLOR)
    line = line.replace("bitset", WBOLD_LIGHT_MAGENTA_COLOR + "bitset" + WBLACK_COLOR)
    line = line.replace("deque", WBOLD_LIGHT_MAGENTA_COLOR + "deque" + WBLACK_COLOR)
    line = line.replace("map", WBOLD_LIGHT_MAGENTA_COLOR + "map" + WBLACK_COLOR)
    line = line.replace("stack", WBOLD_LIGHT_MAGENTA_COLOR + "stack" + WBLACK_COLOR)
    line = line.replace("set", WBOLD_LIGHT_MAGENTA_COLOR + "set" + WBLACK_COLOR)
    line = line.replace("iterator", WBOLD_LIGHT_MAGENTA_COLOR + "iterator" + WBLACK_COLOR)
    line = line.replace("tuple", WBOLD_LIGHT_MAGENTA_COLOR + "tuple" + WBLACK_COLOR)
    line = line.replace("locale", WBOLD_LIGHT_MAGENTA_COLOR + "locale" + WBLACK_COLOR)
    line = line.replace("regex", WBOLD_LIGHT_MAGENTA_COLOR + "regex" + WBLACK_COLOR)
    line = line.replace("istream", WBOLD_LIGHT_MAGENTA_COLOR + "istream" + WBLACK_COLOR)
    line = line.replace("ostream", WBOLD_LIGHT_MAGENTA_COLOR + "ostream" + WBLACK_COLOR)
    
    line = line.replace("cout", WBOLD_CYAN_COLOR + "cout" + WBLACK_COLOR)
    line = line.replace("printf", WBOLD_CYAN_COLOR + "printf" + WBLACK_COLOR)
    line = line.replace("getline", WBOLD_CYAN_COLOR + "getline" + WBLACK_COLOR)
    line = line.replace("cin", WBOLD_CYAN_COLOR + "cin" + WBLACK_COLOR)
    
    line = line.replace("::", WBOLD_LIGHT_YELLOW_COLOR + "::" + WBLACK_COLOR)
    line = line.replace("{", WBOLD_LIGHT_YELLOW_COLOR + "{" + WBLACK_COLOR)
    line = line.replace("}", WBOLD_LIGHT_YELLOW_COLOR + "}" + WBLACK_COLOR)
    line = line.replace("(", WBOLD_LIGHT_YELLOW_COLOR + "(" + WBLACK_COLOR)
    line = line.replace(")", WBOLD_LIGHT_YELLOW_COLOR + ")" + WBLACK_COLOR)
    line = line.replace("*", WBOLD_LIGHT_YELLOW_COLOR + "*" + WBLACK_COLOR)
    line = line.replace("<", WBOLD_LIGHT_YELLOW_COLOR + "<" + WBLACK_COLOR)
    line = line.replace(">", WBOLD_LIGHT_YELLOW_COLOR + ">" + WBLACK_COLOR)
    line = line.replace("+", WBOLD_LIGHT_YELLOW_COLOR + "+" + WBLACK_COLOR)
  
    print(line, end='')

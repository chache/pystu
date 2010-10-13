#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import math
import re
import os
from os.path import join, getsize

def isLeapYear(year):
    '''normal year have no mod when devide by 4 but not 100'''
    '''central year have no mod when devide by 400'''
    if math.fmod(year,100) == 0:
        if int(math.fmod(year,400)) == 0:
            return 1
        else:
            return 0
    else:
        if int(math.fmod(year,4)) == 0:
            return 1
        else:
            return 0

def isMersenne(num):
    l = range(num)
    for n in l:
        if n > 1 and n < num:
            if math.fmod(num,n) == 0:
                print(str(num)+" is not a mersenne")
                return 0
    return 1

def tryWalk(path):
    for root, dirs, files in os.walk(path):
        print root, "consumes",
        print str(int(sum([getsize(join(root, name)) for name in files]))/1024),
        print "Kbytes in", len(files), "non-directory files"
        if 'CVS' in dirs:
            dirs.remove('CVS')  # don't visit CVS directories

if __name__ == '__main__':
    for arg in sys.argv:
        tryWalk(arg)

if __name__ == '__main2__':
    for arg in sys.argv:
        if re.match("^[\d]+$", arg):
            for a in range(int(arg)):
                if isMersenne(a):
                    print(str(a)+" is a mersenne")

if __name__ == '__main1__':  
    for arg in sys.argv:
        if re.match("^[\d]+$", arg):
            '''func to tell is the arg is a valid year'''
            argv = int(arg)
            if isLeapYear(argv) == 1:
                print(arg+" is a leap year")
            else:
                print(arg+" is not a leap year")    

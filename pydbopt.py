#!/usr/bin/env python
'''
    1. read config file and connect to certain database
    2. dump data to csv file or xml file
    3. reload those csv/xml file back to database
'''

import os
import sys
import re

if __name__ == '__main__':
    '''What is about put args to a dictionary? Then we can try to read 
    options. program'''
    args = sys.argv
    print(type(args))
    #for arg in sys.args:
    #    if re.match(".sql",arg):
            



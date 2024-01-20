# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 11:22:18 2024

@author: HP
"""

from firstnotebook import average
average([1,2,3])

dir(average([1,2,3]))

import math
import numpy


import sys

sys.path

import os
path = r'D:\Extra'


os.getcwd()  #: Get the current working directory.
os.chdir(path) #: Change the current working directory.
os.listdir(path)  #: Get a list of files and directories in the given path.
os.mkdir(path)  #: Create a new directory.
#os.remove(file) #: Remove a file.
#os.rmdir(directory)  #: Remove a directory.



# Names Spaces

#Local

def my_function():
    local_variable = "I am in the local namespace"
    print(local_variable)
    print(global_variable)


#Global
global_variable = "I am in the global namespace"



#Built Ins

#len print abs True False init + ==

# https://docs.python.org/3/

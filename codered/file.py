#!/usr/bin/python3
import os
import sys
import shutil
#If you use the code please give credit 
count = 0

#you can take out this while loop, i made it just so the program ran smoother
while count < 3:
    mydir = input("Enter directory name: ")
    count = count + 1
    try:
        shutil.rmtree(mydir)
        break
    except OSError as e:
        print ("Error: %s - %s." % (e.filename, e.strerror))
    if count == 3:
        print("You have ran out of tries")

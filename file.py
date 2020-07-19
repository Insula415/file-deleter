import os
import sys
import shutil

count = 0


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

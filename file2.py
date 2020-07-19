import os
import sys
import shutil

folder = "" #Put the folder name in here


try:
    shutil.rmtree(folder)
except OSError as e:
    print ("Error: %s - %s." % (e.filename, e.strerror))

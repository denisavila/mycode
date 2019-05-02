#!/usr/bin/python3
#Search and stop at first match

import os
import sys

#Search function
def find_all(name, path):
    result = []
    for root, dirs, files in os.walk(path):
            if name in files:
                result.append(os.path.join(root, name))
    return result

lookfor = input("What am I looking for?")
lookwhere = input("What is the path in which to search?")

print(find_all(lookfor,lookwhere))
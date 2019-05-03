#!/usr/bin/env python3
#Author: RZFeeser RZFeeser@alta3.com

"""Script to search for a pattern match"""

import os # used to walk the system
import fnmatch # for regex pattern matching
import pyexcel


EXCLUDE = ["/usr", "/home", "/var"] ## Dont search in these locations


def find(pattern, path):
    """search through filesystem based on given path location"""
    result = []
    for root, dirs, files in os.walk(path, topdown=True):
        if root in EXCLUDE: # if the root matches the exclude list
            dirs[:] = [] # remove the directory list for this iteration
            files[:] = [] # remove the file list for this iteration
        for name in files: # always perform the nested loop, but it maybe empty
            if fnmatch.fnmatch(name, pattern): # if match
                result.append(os.path.join(root, name)) # add to our list
    return result # return the list


# Request data from user
def get_ip_data():
    input_ip = input("\nWhat is the IP address? ")
    input_driver = input("What is the driver associated with this device? ")
    input_3 = input("What is the 3rd col? ")
    input_4 = input("What is the 4th col? ")
    d = {"IP": input_ip, "driver": input_driver, "3dr" : input_3, "4th": input_4}
    return d

# Runtime
mylistdict = []  # this will be our list we turn into a *.xls file





def main():
    """runtime code"""
    lookfor = input("What pattern am I looking for (Example: *.txt or *.cfg) ")
    lookwhere = input("What is the path in which I should search? ")
    print("Results: ", find(lookfor, lookwhere)) # call function





#print("Hello! This program will make you a *.xls file")

#while(True):
#    mylistdict.append(get_ip_data()) # add an item to the list returned by get_ip_data() #{"IP": value, "driver": value}
#    keep_going = input("\nWould you like to add another value? Enter to continue, or enter 'q' to quit: ")
#    if (keep_going.lower() == 'q'):
        break

#filename = "All_The_pys.xls" # input("\nWhat is the name of the *.xls file? ")

#pyexcel.save_as(records=mylistdict, dest_file_name=filename + ".xls")

#print("The file " + filename + ".xls should be in your local directory")



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
    files_result = []
    files_comments = []
    mydict = {}
    mydict1 = {}
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                #result.append(os.path.join(root, name))
                files_result.append(name)
                mydict=({"Name": name,"Location": os.path.join(root, name)})
                result.append(mydict)
    return result


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
    lookfor = "*.py" #input("What pattern am I looking for (Example: *.txt or *.cfg) ")
    lookwhere = "/home/" #input("What is the path in which I should search? ")
    #lookwhere = "/home/student/mycode/Excel_Files" 

    #print("Results: ", [find(lookfor, lookwhere)]) # call function
    mylistdict = find(lookfor, lookwhere)
    print(mylistdict)
    filename = "All_The_pys.xls"    
    pyexcel.save_as(records=mylistdict, dest_file_name=filename )


main()





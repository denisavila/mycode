#!/usr/bin/env python3

## sudo apt install python3-pip

## python3 -m pip install pyexcel
## python3 -m pip install pyexcel-xls
import pyexcel

# Request data from user
def get_ip_data():
    input_ip = input("\nWhat is the IP address? ")
    input_driver = input("What is the driver associated with this device? ")
    d = {"IP": input_ip, "driver": input_driver}
    return d

## This code is left turned off, but might help visualize how pyexcel works with data sets.
## IP is the first column, whereas driver is the second column.
## mylistdict = [ {"IP": "172.16.2.10", "driver": "arista_eos"}, {"IP": "172.16.2.20", "driver": "arista_eos"} ]
## pyexcel.save_as(records=mylistdict, dest_file_name="ip_list.xls")

varfilename = input('What is hte name of the file? D no include extension')
myexcelval = {}

varfilename = varfilename + ".xls"
#Dump the spreadsheet in format 
excelrecords = pyexcel.iget_records(file_name=varfilename)

for x in excelrecords:
    totalsocket = x['ip'] + ":" + str(x['port'])
    myexcelval.update ( {x['service']:totalsocket}) ## add new IP and driver
print(myexcelval)

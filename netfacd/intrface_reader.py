#!/usr/bin/env python3
"""Desc here """
import netifaces
print(netifaces.interfaces())

for i in netifaces.interfaces():
    print('\n**********Details of Interface - ' + i + ' ****************')
    #print(netifaces.ifaddresses(i))
    
    try:
        print('MAC: ', end = ' ')
        print(netifaces.ifaddresses(i)[netifaces.AF_LINK][0]['addr'])#Print MAC
        print('IP: ', end = ' ')
        print(netifaces.ifaddresses(i)[netifaces.AF_INET][0]['addr'])# Print IP
    except:
        print('Could not collect adapter information') #Error line
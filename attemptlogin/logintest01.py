#!/usr/bin/env python3
"""
Code for Login Fails
"""
loginfail = 0
fromIP= []
keystone_file = open ('/home/student/mycode/attemptlogin/keystone.common.wsgi','r')
keystone_file_lines = keystone_file.readlines()

for i in range(len(keystone_file_lines)):
    if " - - - - -] Authorization failed" in keystone_file_lines[i]:
        loginfail += 1
        fromIP.append(keystone_file_lines[i][-11:])
        print(fromIP)
print('The number of failed log in attempts is ' + str(loginfail))
print(fromIP)
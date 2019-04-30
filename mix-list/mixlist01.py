#!/usr/bin/env python.py
my_list = ["192.168.0.5",5060,"UP"]
print("The first itemin the list (IP): " + my_list[0])
print("The second itemin the list (Port): " + str(my_list[1]))
print("The third itemin the list (state): " + my_list[2])
#Comment
new_list = [5060, "80", 55, "10.0.0.1","10.20.30.1","ssh"]
print("When I " , new_list[5] ," into IP addresses ", new_list[3], " or " , new_list[4], "I am unable to ping ports", new_list[0], new_list[1], new_list[2]) 
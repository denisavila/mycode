#!/usr/bin/env python3
ipchk = input('Apply an IP Address:') # prompt for IP

if ipchk=='192.168.70.1': 
   print("Looks like the IP address was set: " + ipchk + ' This is not recommended.')
elif ipchk:
   print (' Looks like an IP was provided and was set to: ' + ipchk )
else:
   print('You did not provide an IP')
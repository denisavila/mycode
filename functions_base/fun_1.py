#!/usr/bin/env python3

def word_counter(a,b):
   print("This is out word coutner function")
   print( a,b)

def last_funct():
   print("this is the end")

def get_names():
    a = 'sol.txt'
    b = 'out.txt'
    return a,b

def main():
   print("Starting main")
   x = get_names()
   word_counter()
   last_funct()

main()
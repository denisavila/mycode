#!/usr/bin/env python3
"""
Code for Factorials
"""
X = int(input("Enter a number:"))
F = 1
for i in range(1, X+1):
    print(i)
    F = F * i
print(X, '! = ', F)

#!/usr/bin/python3
from blessings import Terminal
t = Terminal()
print(t.clear())

def yellow_np():
    print(t.bold_red_on_bright_yellow('It hurts my eyes!'))

def yellow_wp(p):
    print(t.bold_red_on_bright_yellow(p))

def trx(p):
    X = t.width - len(p)
    return int(X)


yellow_np()

yellow_wp('Passing text to be formatted')

x = trx("Test text 2")
print(x)
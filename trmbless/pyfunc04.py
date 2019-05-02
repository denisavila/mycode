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

def top_right(p):
    with t.location(trx(p),0):
        yellow_wp(p)


def prompt(p):
    with t.location(0,t.height-2):
        print(t.reverse(p))
    with t.location(len(p) + 1, t.height-2):
        orders = input()
    return orders


top_right("Print on top Right!!!")

orders = prompt("Prompt on bottom left:")
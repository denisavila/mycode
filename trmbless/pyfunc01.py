#!/usr/bin/python3
from blessings import Terminal
t = Terminal()
print(t.clear())
print(t.bold("Hi, There!!"))
print(t.move_down)
print(t.bold_red_on_bright_green('It hurts my eyes!'))
print(t.move_down+t.bold_underline_black_on_bright_yellow('It hurts my eyes! blinking'))
print(t.move_down)
print("Terminal Width", t.width)
print("Terminal height", t.height)
print(t.move_down)
print(t.move_down)
print("one line for Terminal Width and hight",t.reverse, t.width, t.height)
with t.location(20, t.height - 1):
	print(t.reverse+t.blink('Blinking in REVERSE!!!!! '))
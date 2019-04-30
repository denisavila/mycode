#!/usr/bin/env python

#loops

for i in range(10):
	print(i, end=' ')

for z in range(10):
	print(z, end=':)  ')



animals = ["dog", "cat","squirrel","hamster"]
for animal in animals:
	print (animal)

rope = "braided"

for x in rope:
	print(x)

foo = open("outfile.txt","w")
print('You must custruct additional pylons.', file=foo)

foo.close()

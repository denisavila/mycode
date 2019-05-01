#!/usr/bin/env python3
######## Scan for words ##########
## 
datafile = open("sol.txt", "r")


## display file to the screen - .read()
#print(datafile.read())

## close file
#datafile.close()

######## EXPLORE READLINES ##########
## re-create file object to explore new method
#datafile = open("sol.txt", "r")

## make a list of file lines - .readlines()
datafile1 = datafile.read().replace('\n',' ')
#print(datafile1)

listwords = datafile1.split(" ")

#print(listwords)
list2 = []

for x in listwords:
     #print(x)
     if x not in list2:
        list2.append(x)

print(list2)
print(len(listwords))
print(len(list2))

my_dict = {i:listwords.count(i) for i in listwords}

print(my_dict)

my_dic2 = {}

print("method2:")
for item in list2:
    num = {item: listwords.count(item)}
    #print(num)
    my_dic2.update(num)

print(my_dic2)

    
v = input("What qord do you want to search for:")
print(my_dic2[v])

## Always close your file
datafile.close()

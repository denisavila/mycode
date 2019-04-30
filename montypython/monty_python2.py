#!/usr/bin/env python3
round = 0

while True:
    round = round +1
    print('Finish the movie title, "Monty Python \'s The life of ______ "')
    answer = input()
    if( answer.lower() == 'brian'):
       print("Correct")
       break
    elif(round==3):
       print("Sorry, the answer was Brian")
       break
    elif( answer == 'shrubbery'):
       print("You have given the secret answer!!!")
       break
    else:
       print("Sorry try again")


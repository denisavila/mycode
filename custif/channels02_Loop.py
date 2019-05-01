#!/usr/bin/env python3
print('Channel Selection')

print('')
favs = [26,52,4,498,102]

for a in favs:
            print(a)
            a = int(a)
            if a <= 600 and a >=201:
              pack = 5
              message = "Select Pachage 5 Channels 201 - 600"
            elif a <=200 and a >=101:
              pack = 4
              message = "Select Pachage 4 Channels 101 - 200"
            elif a <=100 and a >40:
              pack = 3
              message = "Select Pachage 3 Channels 1 - 100"
            elif a <=40 and a >10:
              pack = 2
              message = "Select Pachage 2 Channels 1 - 40"
            elif a <=10:
              pack = 1
              message = "Select Pachage 1 Channels 1 - 10"
            else:
              message = "select a channel less that 600"
            print(message)

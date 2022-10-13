
# open file (if exists, if not create it)
# write user imput to it (append or write)

import os
from os.path import exists

user_input = input("What to write: ")
#path = os.getcwd()
#print(path)

file_exists = exists("write.txt")

if file_exists is False:
    f = open("write.txt", "w")
    f.write(user_input)
    f.close()
else:
    f = open("write.txt", "a")
    f.write(user_input)
    f.close()

#open and read the file after the appending:
f = open("write.txt", "r")
print(f.read())

# input = input("What to write: ")

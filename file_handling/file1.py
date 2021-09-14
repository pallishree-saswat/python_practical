# File access Modes
# File handle is like a cursor, which defines from where the data has to be read
# or written in the file.
# there are 6 access modes in python
# the handle is positioned at the begining of file


# Read Only(r):
# Open text file for reading.If the file doesnt exist, raise i/o error.
# This is also default mode in which file opened
# The handle is positioned at beginging of file

# Read and Write(r+):
# Open for reading and writting
# Open text file for reading.If the file doesnt exist,
#  raise i/o error.

# Write Only(w):
# Open the file for writting
# Create the file if doesnt exist
# the handle is positioned at the begining of file
# return an integer which means the number of bytes wriiten or present
# i that file

# Write and read(w+):
# open for reading and writing
# For existing file data is truncated and over written.
# the handle is positioned at the begining of file

# Append only(a):
# opne the file for writing.
# Create the file if doesnt exist
# the handle is positioned at the ending of file
# Data being written will be insterted at the end of exist data


# Append and read(a+)
# open for reading and writing

import os
fn = "./hello.txt"
print(os.path.exists(fn))

file = open(fn, "r")
# print(file.read())
print(file.read(4))  # read only first 4 bytes
file.close()

file2 = open("new.txt", "w")
x = file2.write("Hello from other side")
print(x)
file.close()

file3 = open("./word.txt", "r")
print(file3.readlines())  # read line by line

print(file3.read())  # will get nothing as python read everything from begin to end
print(file3.seek(5))  # it will move cursor to a position

print(file3.read())  # now it can from that position again
file3.close()  # always remember to close a file otheewise you will get nothing


# read file with with statements
# the with statement simplifies exception handling by encapusulation
# common preparation and clean up tasks
# It will automatically close the file


with open("./with.txt", "r") as newFile:
    print(newFile.read())
    newFile.seek(5)
    print(newFile.read())

# newFile.read() it will cause err if you try to call outside of with block
""" 
with open("hello2.txt","r") as fileHello:
    print(fileHello.read()) """


import json

with open("failed.txt", "w") as outfile:
    outfile.write(json.dumps(["name"]))


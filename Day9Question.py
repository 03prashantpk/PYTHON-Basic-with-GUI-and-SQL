'''WAP to Create a new File if the file already exist, change the file n
and create a new file automatically'''

# Import string and random module
import string
import random

try:
    f = open("Experimental Files/fileexist2.txt", "x")
    f.close()
except: 
    newname =  random.choice(string.ascii_letters)
    f = open("Experimental Files/fileexist",newname,".txt", "a")
    f.close()


# f = open("Experimental Files/fileexist2.txt", "a")
# f.close()

# fileexist = open("Experimental Files/fileexist2.txt", "r")
# fileexist.close()

# if(fileexist == " "):
#     print("File Exist")
#     f = open("Experimental Files/fileexist2.txt", "a")

# else:
#     f = open("Experimental Files/fileexist2.txt", "a")
#     f.close()
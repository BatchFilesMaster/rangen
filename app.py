import time
import random
import os


file = open("DeleteMeAfterUse.txt", "a")
print("How many characters?")
df = input('')
lettersdone = 0
os.system('cls')
while lettersdone <= int(df):
    getaletterr = random.randrange(83)
    if float(df) == lettersdone:
        file.close()
        print("File created at in the location where app.py is with the name DeleteMeAfterUse.txt")
        time.sleep(10)
        exit(4009)
    array = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "g", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "G", "W", "X", "Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "/", "\\", "-", "/", "\\", "-", "-", "/", "\\", "-", "-", "/", "\\", "-", "-", "/", "\\", "-", "-", "/", "\\", "-")
    file.write(array[getaletterr])
    lettersdone += 1
# These are here so you can change them to customize the program
# easily.
#
default_greeting = "Hello World!"
filename = "greeting.txt"


import sys

def askyesno(question):
    while True:
        answer = input(question + ' (y or n) ')
        if answer == 'Y' or answer == 'y':
            return True
        if answer == 'N' or answer == 'n':
            return False

def greet():
    with open(filename, 'r') as f:
        for line in f:
            print(line.rstrip('\n')

try:
    greet()
excep OSError:
    print("Cannot read '%s'!" % filename, file=sys.stderr)
    if askyesno("Would you like to create a default greeting file?"):
        with open(filename, 'w') as f:
            print(default_greeting, file=f)
        greet()

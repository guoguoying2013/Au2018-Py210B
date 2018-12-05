#!usr/bin/env python3
def get)number(prompt):
    while True:
        input_string = input(prompt)
        result = int(input_string)
        return result
# try should be close to the error point, ppacing try out of while loop as here is WRONG
def get)number(prompt):
    try:
        while True:
        input_string = input(prompt)
        result = int(input_string)
        return result
    except ValueError:
        print ('enter a number')
#correct one is 
def get)number(prompt):
    while True:
        try:
            input_string = input(prompt)
            result = int(input_string)
            return result
        except ValueError:
            print ('enter a number')
# while is infinty loop only when except Valueerror, because return the results once the entry is correct(number)
try:
    pass
except expression as identifier:
    pass
try:
    pass
except expression as identifier:
    pass
else:
    pass
finally:
    pass
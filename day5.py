import string
import termios
import compound
from importlib import reload
reload(compound)
from compound import *

def cut(start, code):
    newCode = code[0:start] + code[start+2:]
    return newCode

newCode = code + ""    

def doSomething(inputCode):    
    didSomething = True

    
    while didSomething:
        didSomething = False
        for index, letter in enumerate(inputCode):
            upper = True
            if index != len(inputCode) - 1 and index != len(inputCode) - 2:
                if inputCode[index + 1].upper() == letter.upper():
                    if letter.isupper():
                        if inputCode[index + 1].islower():
                            inputCode = cut(index, inputCode)
                            didSomething = True
                            break
                    elif letter.islower():
                        if inputCode[index + 1].isupper():
                            inputCode = cut(index, inputCode)
                            didSomething = True
                            break
            elif index == len(inputCode) - 2:
                if inputCode[index + 1].upper() == letter.upper():
                    if letter.isupper():
                        if inputCode[index + 1].islower():
                            inputCode = inputCode[:-2]
                            didSomething = True
                            break
                    elif letter.islower():
                        if inputCode[index + 1].isupper():
                            inputCode = inputCode[:-2]
                            didSomething = True
                            break
            else:
                break
            
    return len(inputCode)
            
            
def evaluate(code):
    lengths = {}


    
    for letter in string.ascii_lowercase:
        newCode = list(code)
        
        lower_count = newCode.count(letter)
        upper_count = newCode.count(letter.upper())

        

        while min(lower_count, upper_count) > 0:
            for char in newCode:
                if char == letter:
                    newCode.remove(char)
                    break
            for char in newCode:
                if char == letter.upper():
                    newCode.remove(char)
                    break
                
            lower_count -= 1
            upper_count -= 1

        lengths[letter] = doSomething(newCode)

    print(lengths)
            
evaluate(code)

import random

def multiply(a, b):
    return a * b
    
def subtract(a, b):
    return a - b
    
def add(a, b):
    return a + b
    
def divide(a, b):
    return a / b
    
def chooser(a, b):
    rand = random.randint(1, 4)
    if rand == 1:
        num = multiply(a, b)
        op = '*'
    elif rand == 2:
        num = divide(a, b)
        op = '/'
    elif rand == 3:
        num = add(a, b)
        op = '+'
    elif rand == 4:
        num = subtract(a, b)
        op = '-'
    chosen = [num, op]
    return chosen
        

def runGame():
    x = float(raw_input("Please enter an integer: "))
    y = float(raw_input("Please enter another integer: "))
    z = float(raw_input("Please enter the last integer: "))
    if x == 0 or y == 0 or z == 0:
        print "I told you not to use 0, you son of a bitch."
        quit()
    #first operation
    firstNum = chooser(x, y)
    secondNum = chooser(firstNum[0], z)
    print "The final number is: %f" % (secondNum[0])
    answerOne = raw_input("What was the first operator? \n")
    answerTwo = raw_input("What was the second operator? \n")
    if answerOne == firstNum[1] and answerTwo == secondNum[1]:
        print "That's right! Congratulations!"
    else:
        print "Wrong! The answer was %s and %s" % (firstNum[1], secondNum[1])
    playAgain = raw_input("Play Again? \n")
    if playAgain == 'yes' or playAgain == 'Yes' or playAgain == 'y':
        runGame()
    else:
        print "Goodbye!"
        quit()
    
    
def open():
    print "\nWelcome to this shitty little command-line game! \n"
    print "To play, you must give the computer 3 integers - NOT ZERO!\nThe computer then processes them randomly, and you need to guess what it did!\n"
    print "The operators the computer uses are *, /, - and +. Good luck!\n"
    v = raw_input("Would you like to start the game?\n")
    if v == 'yes' or v == 'y' or v == 'Y':
        runGame()
    else:
        print "... just say yes ..."
        
open()
    

   
    

youguess=False #Initializing the variables
numtries=0
while youguess==False: #This means that the while loop will repeat itself infinitely until the user inputs the integer 974(0.01% of getting it correct)
    numtries=numtries+1 
    correct=974
    guess=input("Type a number between 1-1000(example:500):")
    numguess=int(guess) #Converting a string input to the form of an integer
    if(numguess==correct):
        str_tries=str(numtries)
        print("Well done!")
        print("You have solved the problem in "+str_tries +"tries.")
        youguess=True
    else:
        if (numguess>correct):
            print("Wrong!Too high.")
        else:
            print("Wrong!Too low.")
            

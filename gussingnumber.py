import random

target = random.randint(1,100)

while True:
    userChoice = input("Guess the target or Quit(Q):")
    if(userChoice =="Q"):
        break

    userChoice = int(userChoice)
    if(userChoice == target):
        print("sucess : correct Guess!!")
        break
    elif(userChoice<target):
        print("your number was too small.take a bigger guess..")
    else:
        print("your number wass too big> take a smaller guess..")



print("_____game over_____")
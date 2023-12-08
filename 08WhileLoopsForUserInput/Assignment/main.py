import random

def number_guesser():
    print("number gusser")
    number= random.randint(1, 10)
    response= int(input("enter a number betwwen 1-10:"))
    while response!= number:
        print("Wrong try agan")
        response= int(input("enter a number betwwen 1-10:"))
    else:
        print("Correct")
print("#######################")

def number_guesser_with_lives():
    lives = 3
    number2  = random.randint(1, 10)
    response2 = int(input("enter a number betwwen 1-10:"))
    if lives == 0:
        print("game over")
    while response2 != number2 and lives > 0:
        print("Wrong try again")
        response = int(input("enter a number betwwen 1-10:"))
        lives = lives-1
        print("you have this many lives left=",lives)
        if lives < 1:
            print("game over")
            print("#######################")
        else :
         print("Correct")


number_guesser_with_lives()

def vending_machine(snack):
    amountdue = 50
    coin= int(input("enter a coin- 25,10, or 5"))
    while amountdue== 50:
        print("Amount Due:",amountdue)

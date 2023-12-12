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
        if lives <1:
            print("game over")
        elif lives== 0:
            print("game over")
    else :
         print("Correct")


#number_guesser_with_lives()

def vending_machine():
    change=0
    amountdue = 50
    coin= int(input("Enter a coin: 25, 10, or 5:"))
    while amountdue >= 0:
        print("Amount Due:",amountdue)
        if amountdue<0:
           change = amountdue * -1
           print("your change:",change)
        elif coin== 25 or coin== 10 or coin== 5:
            amountdue = amountdue- coin
            print("Amount due:",amountdue,"cents")
        coin= int(input("enter a coin- 25, 10, or 5:"))
   
        
vending_machine()

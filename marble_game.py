#Marble game
import random
import math

#Initialize the marble bag
marble_bag = ["green"]*5 + ["red"]*3 + ["black"] + ["white"]
random.shuffle(marble_bag)
print(marble_bag)

coins = 1000

while True:
    try:
        n_rounds = int(input("Enter how many rounds you wish to play: "))

    except:
        print("Invalid Input")
    
    else:
        break

for i in range(n_rounds):
    while True:
        try:
            user_bet = abs(int(input(f"You have {coins}. How much do you want to bet? ")))

        except:
            print("Invalid Input")
        
        else:
            break
    
    coins -= user_bet
    marble = random.choice(marble_bag)

    print(f"You drew {marble}")
    if(marble == "green"):
        print(f"You win {user_bet} coins back")
        coins += 2*user_bet
    
    if(marble == "red"):
        print(f"You loose {user_bet} coins back")

    if(marble == "black"):
        print(f"WOOOOHOOOO You lucky bastard! You win {user_bet}x10 babiii!!!")
        coins += user_bet * 10
    
    if(marble == "white"):
        print(f"Womp Womp you loose {user_bet*5}")
        coins -= user_bet*5
        print(f"Your coin count is {coins}")
        break

    print(f"Your coin count is {coins}")
    print()

    if(coins <= 500):
        print(f"Your coin count is below 500")
        print("Game Over")
        break
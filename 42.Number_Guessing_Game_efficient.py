            #Efficient but Above is more perfect

import random
winning_number = random.randint(1 , 100)
guess = 1
#game_over = False

while True:
    number = int(input("Guess a number between 1 and 100: "))
    if number == winning_number:
        print(f"You win and you guessed this number in {guess} times")
        break
    else:
        if number < winning_number:
            print("Too low !")
        else:
            print("Too high !")
            
        guess +=1
        continue

#Guessing game

#For this simple game what we need to do is ask for user to type a random number between 1 and 100
#After that we'll answer to user if he chousen the right number

import random
import math
numbers = []
for n in range(1, 101):
     numbers.append(n)
     
under = 0
high = len(numbers) - 1
random_number = random.randrange(0, len(numbers)-1)
meedle = math.ceil((high - under)/2)
print(f"The number is {random_number}")

while True:
    guess = int(input("Type a number between 1 and 100: \n"))
    if guess < 1 and guess > 100:
        print("Becarefull the number needs to be between 1 and 100.")
    if guess == random_number:
        print("Congratulations you've guessed the secret number")
        break
    if guess > random_number:
        high = math.ceil(meedle - 1)
        numbers = []
        print(f'The number is lower then {guess}')
        for n in range(1, meedle +1):
            numbers.append(n)
    if guess < meedle:
        under = math.ceil(meedle + 1)
        numbers = []
        print(f'The number is higher than {guess}')
        for n in range(1, meedle +1):
          numbers.append(n)
    while True:
        guess_again = input("Do you want to try again? Y/N \n").lower()
        if guess_again != 'y' and guess_again != 'n':
            print("You need to answer with Yes(Y) or No(N)")
        if guess_again == 'y' or guess_again == 'n':
            break 
    if guess_again == 'n':
        print("Thanks for played our simple game.")
        break

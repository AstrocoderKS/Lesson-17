# Activity 1
import random
Number = str(random.randint(0,9))
print("I will generate a number between 0 and 9. You have a tenth of chance to guess the correct number.")
print("You win the game if you guess the correct number. Best of luck!")
while True:
    Guess = str(input("Guess a number."))
    if Number == Guess:
        print("Well done. You have correctly guessed the answer.")
        break
    else:
        print("Incorrect. Try again.")


# Activity 3
import math
print(math.sqrt(2048))
print(math.ceil(1.69))
print(math.floor(1.96))
print(math.copysign(8,-19))
print(math.gcd(5192, 5104))
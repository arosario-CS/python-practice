from ast import Break
from multiprocessing.resource_sharer import stop


number = 9
i=0
while i < 3:
    guess = int(input("Guess the magic number: "))
    i = i + 1
    if guess == number:
        print("YOU WIN")
        break
else:
    print("YOU LOSE")

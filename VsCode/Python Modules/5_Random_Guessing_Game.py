import sys
from random import randint

start = int(sys.argv[1])
end = int(sys.argv[2])
random_number = randint(start,end)

def guessing_game(start,end,random_number):
    counter = 0
    while True:
        try:
            number = int(input(f"Guess the Number ({start} - {end}) : "))
            counter += 1 
            if number == random_number:
                print(f"\n Hurray! You Guessed it Correctly in {counter} Attempt")
                break
            elif number < random_number:
                print("Oops You Guessed it Wrong , Try Again\n")
                if (end - start > 25):
                    print("Number is Higher\n")
                    continue

            elif number > random_number:
                print("Oops You Guessed it Wrong , Try Again\n")
                if (end - start > 25):
                    print("Number is Smaller\n")
                    continue
        except ValueError as err:
            print(f"Something Went Wrong, Error : {err}")
    
guessing_game(start,end,random_number)
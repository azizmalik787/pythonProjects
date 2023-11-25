import random


def guess(x):
    random_number = random.randint(1, x)
    number = 0
    while number != random_number:
        number = int(input(f"Please enter the number between 1 and {x}: "))
        if number > random_number:
            print("Try again, your guess is Too High.")
        elif number < random_number:
            print("Try again, your guess is Too Low.")
    print(f"You have successfully guessed the number i.e. {number}.")


def computer_guess(x):
    low = 1
    high = x
    random_number = random.randint(low, high)
    c_guess = 0
    feedback = 'a'
    while feedback != 'c':
        if low != high:
            c_guess = random.randint(low, high)
        else:
            c_guess = high  # case where low = high
        feedback = input(f"Is guess {c_guess} is too High (H), too Low (L), Correct (c)?").lower()
        if feedback == 'l':
            low = c_guess + 1
        elif feedback == 'h':
            high = c_guess - 1
    print(f"Yayyyy!!! The Computer guessed the number correctly {c_guess}.")


upper_bound = int(input("Set the upper range of the guessing game: "))
driver = input("Who is the guesser, You (Y) or the Computer(C)?").lower()
if driver == 'y':
    guess(upper_bound)
else:
    computer_guess(upper_bound)

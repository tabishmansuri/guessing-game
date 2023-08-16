import random


while True:
    number = random.randint(1,100)
    
    try:
        guess = int(input("Enter a guess number : "))
        while guess != number:
            if guess > number:
                guess = int(input("Choose a smaller number : "))
            elif guess < number :
                guess = int(input("Choose a larger number : "))

        if guess == number :
            print(f"Congratulation ! your guess {number} is correct")

    except ValueError:
        print("Oops! Plaese enter a Number")

    q = input("Do you want to play again!  y/n : ").lower()
    if q[0] == ("n"):
        break

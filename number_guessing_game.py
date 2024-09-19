from random import randint

def play():
    lower_num, higher_num = 1, 10
    random_number = randint(lower_num, higher_num)
    print(f"You have 3 turns, Guess the number in the range from {lower_num} to {higher_num}")
    count =3 # Number of attempts
    while count > 0:
        try:
            # User input
            user_guess = int(input("Guess: "))

            # Ensure guess is within range
            if user_guess > higher_num or user_guess < lower_num:
                print(f"The values must be in range between {lower_num} and {higher_num}")
                continue

        except ValueError:
            print("Please enter a valid number.")
            continue
    
        # Check if guess is correct, Provide hints for incorrect guesses
        if user_guess > random_number:
            print("Your guess is incorrect, the number is lower")
        elif user_guess < random_number:
            print("Your guess is incorrect, the number is higher")
        else:
            print(f"You Guessed it right, the number is {random_number}")
            break

        # Decrement the count for incorrect guesses
        count -= 1

        # Provide feedback and remaining turns
        if user_guess != random_number and count == 2:
            print("You have two turns left")
        elif count == 1:
            print("You have one turn left")  
        elif count == 0:
            print(f"You ran out of chances! The correct number was {random_number}")
            break
play()
while True:
    play_again = input("Play Again? Y/N: ").lower()
    if play_again == "y":
        play()
    elif play_again == "n":
        print("Thank you for playing")
        break
    else:
        print("Please select a valid choice (Y/N)") 
        continue

    





            

        



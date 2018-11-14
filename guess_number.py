from random import randint

play = True

user_name = raw_input("What is your name?:\n")
while play is True:
    random_num = randint(1, 10)
    number_guessed = False
    iterations = 0
    print("Ok " + user_name + ", I am thinking of a number between 1 and 10\n")
    print(str(random_num) + "\n")

    while number_guessed is False:
        guess = raw_input("Can you guess what it is?\n")
        
        iterations += 1 
        
        if int(guess) == int(random_num):
            number_guessed = True
        elif int(guess) < random_num:
            print("You guessed " + str(guess) +". Try a higher number\n")
        elif int(guess) > random_num:
            print("You guessed " + str(guess) +". Go lower\n")
    if iterations == 1:
        print("You got it " + user_name + "! First try!")
    else:
        print("You got it " + user_name + "! It took " + str(iterations) + " guesses!")
    play_again = raw_input("Play again? y/n:\n")
    if play_again != 'y':
        print("Bye " + user_name + ". I'm watching you...")
        quit()

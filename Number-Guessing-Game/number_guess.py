import random
attempt_list = []

def show_score():
    if(len(attempt_list)) <= 0:
        print("There is currently no high score!")
    else :
        print("The current highscore is {} attempts".format(min(attempt_list)))

def is_num(g, n):
    if g == n:
        return True
    elif g > n:
        print("Number is smaller!")
        return False
    else:
        print("Number is higher!")
        return False

def start_game():
    attempts = 1
    n = int(random.randint(1,10))
    flag = True
    while flag:
        guess = int(raw_input("Guess a number: "))
        while guess < 1 or guess > 10:
            guess = int(raw_input("Invalid! Choose a number between 1 to 10:  "))
        if is_num(guess, n):
            attempt_list.append(attempts)
            print("Yay! Found it")
            flag = False
        else:
            attempts += 1
    
    print("You guessed the number in " + str(attempts) +  " attempts")
    show_score()
    again = raw_input("Want to play again? ")
    if again.lower() == "yes":
        start_game()
        

print("Welcome to the Game")
user_name = raw_input("Your name: ")
print("Hi " + user_name)
print("Lets start")
start_game()

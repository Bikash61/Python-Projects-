import random

user_wins = 0
computer_wins = 0

options = ['rock', 'paper', 'scissor']

while True:
    user_input = input("Enter any one Rock/Paper/Scisoor or q to quit: ").lower()
    if user_input == 'q':
        break
    if user_input not in options:
        continue
    random_number = random.randint(0,2)
    computer_pick = options[random_number]
    print("Computer Pick is ", computer_pick+'.')
    if computer_pick == 'rock' and user_input == 'scissor':
        print("Computer wins")
        computer_wins +=1
    
    elif (computer_pick == 'paper' and user_input == 'scissor'):
        
        print("User wins")
        user_wins +=1
    
    elif computer_pick == 'scissor' and user_input == 'scissor':
        print("Game draw")
    elif computer_pick == 'rock' and user_input == 'paper':
        print("User wins")
        user_wins += 1
    elif computer_pick == 'paper' and user_input == 'paper':
        print("Game Draw")
    elif computer_pick == 'scossor' and user_input == 'paper':
        print("Computer Wins")
        computer_wins +=1
    elif computer_pick == 'rock' and user_input == 'rock':
        print("Game draw")
    elif  computer_pick == 'paper' and user_input == 'rock':
        print("Computer Wins")
        computer_wins +=1
    elif computer_pick == 'scissor' and user_input == 'rock':
        print("User Wins")
        user_wins +=1
    else:
        print("Invalid")
    break
print("The result is Computer score:",  computer_wins, "and user score is", user_wins)
print("Thank you for your time")

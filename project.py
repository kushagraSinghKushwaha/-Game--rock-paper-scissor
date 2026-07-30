import random 
choices = ["rock","paper","scissors"]
user_choice = input("chosse rock or paper or scissors: ").lower()
computer_choice = random.choice(choices)
print(f"computer choice : {computer_choice}")
if user_choice == computer_choice:
   print("it is a tie")
elif(user_choice == "rock" and computer_choice == "scissors") or \
    (user_choice == "scissors" and computer_choice == "paper") or \
    (user_choice == "paper" and computer_choice == "rock"):
     print("you win")
else:
    print("you loose")

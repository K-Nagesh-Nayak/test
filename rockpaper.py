import random
choice=("ROCK","PAPER","SCISSORS")
x=True  #check for loop
c_s=0   #computer score
p_s=0   #player score

n=int(input("best of 3,5,9 or your choice "))
Player=input("Your game name: ").upper()
while x:
    player_choice=None  #initial value
    comp=random.choice(choice)
    while player_choice not in choice: #to check input 
        player_choice=input("Enter your choice(ROCK,PAPER,SCISSORS): ").upper()
    print(f"Player choice: {player_choice} & Computer choice: {comp} ")
    if player_choice==comp:
        print("its a tie")
    elif player_choice=="ROCK" and comp=="SCISSORS":
        print("you won")
        p_s+=1
    elif player_choice=="SCISSORS" and comp=="PAPER":
        print("you won")
        p_s+=1
    elif player_choice=="PAPER" and comp=="ROCK":
        print("you won")
        p_s+=1
    else:
        print("computer won")
        c_s+=1
    if c_s==n or p_s==n: 
        x=False
        if c_s==n:
            print("The final score")
            print(f"Computer:{c_s} & {Player}:{p_s}")
            print("Computer won")
        else:
            print("The final score")
            print(f"Computer:{c_s} & {Player}:{p_s}")
            print("You won")

        

    

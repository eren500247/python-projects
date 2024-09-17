import random

print("Welcome To Rock,Paper,Scissors Games")


while True:
    user_input = input('Choose Your Weapons (Rock,Paper,Scissors) : ')

    r_weapon_list = ["Rock","Paper","Scissors"]

    robot_weapon = r_weapon_list[random.randrange(len(r_weapon_list))]


    if user_input == robot_weapon:
        print("Tie")  
    elif user_input == "Rock":
        if robot_weapon == "Scissors":
            print("You Win🏆")
        else:
            print("You Lose🥲")
    elif user_input == "Paper":
        if robot_weapon == "Rock":
            print("You Win🏆")
        else:
            print("You Lose🥲")
    elif user_input == "Scissors":
        if robot_weapon == "Paper":
            print("You Win🏆")
        else:
            print("You Lose🥲")
    else:
        print("Invalid Weapon")
    
    print(f"You Choose : {user_input}")
    print(f"Robot Choose : {robot_weapon}")
        
    a = input("Do you want to play again? : ")
    
    if a.lower() != "yes":
        print("Thank You!")
        break
        
        

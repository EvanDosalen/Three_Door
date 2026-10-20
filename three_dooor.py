#Name: Evan Jane L. Dosalen
#Date: October 20, 2026

starting_points = 20

def display_intro():
    print("===================================")
    print("Three Door Treasure Hunt!")
    print("===================================")

#Define
def show_doors():
    print("Choose a door: [1]Wooden Door, [2]Red Door, [3]Golden Door")

#Define explore_door to compute the total scores
def explore_door(choice, player):
    if choice == 1:
        print("Congratulations! You found the treasure chest!")
        print("+50 points")
        score = starting_points + 50
        display_result(player, score)
    elif choice == 2:
        print("You disturbed the dragon! Better luck next time.")
        print("-20 points")
        score = starting_points - 20
        display_result(player, score)
    elif choice == 3:
        print("Congratulations +30 points! You found the magical key!")
        print("+30 points")
        score = starting_points + 30
        display_result(player, score)

    else:
        print("Please enter a valid choice.")

#Display the results from the player's choice.
def display_result(player, score):
    print("-------------Game Results-------------")
    print(f"Player: {player} Starting points: {starting_points}")
    print(f"Your score is: {score}")

    if score >= 70:
        print("You are a Treasure Master")
    elif score >= 40 and score <= 69:
        print("You are a Brave Explorer")
    elif score < 40:
        print("You are still a Beginner Adventurer")

#Call the programs.
display_intro()
player_name = input("Enter your name: ")
show_doors()
door_choice = int(input("Enter your choice: "))
explore_door(door_choice, player_name)



import random

# List of valid colors
valid_colors = ["red", "blue", "green", "yellow", "orange", "purple", "pink", "white", "black"]

def color_game():
    print("Welcome to the color game>>>")
    player_name = input("Please enter your name for the score board: ")
    
    games_won = 0
    games_lost = 0
    
    while True:
        print("\n1> Start Game")
        print("2> Exit")
        choice = input("Enter your choice: ")
        
        if choice == "2":
            print("Thank you for playing! Goodbye!")
            break
        elif choice == "1":
            machine_color = random.choice(valid_colors)
            attempts = 5
            game_won = False
            
            while attempts > 0:
                user_color = input("Please enter a color: ").strip().lower()
                
                if user_color not in valid_colors:
                    print("Invalid color. Please try again with a valid color.")
                    continue
                
                if user_color == machine_color:
                    print(f"You won the game!")
                    print(f"Number of attempts: {6 - attempts}")
                    game_won = True
                    games_won += 1
                    break
                else:
                    attempts -= 1
                    print(f"Your guess was wrong. Please try again.")
                    print(f"Number of attempts left: {attempts:02}")
            
            if not game_won:
                print("You've used all attempts. Better luck next time!")
                print(f"The correct color was: {machine_color}")
                games_lost += 1
            
            while True:
                print("\n1> See Score Board")
                print("2> Play Again")
                print("3> Exit")
                post_game_choice = input("Enter your choice: ")
                
                if post_game_choice == "1":
                    print("\n--- Score Board ---")
                    print(f"Player Name: {player_name}")
                    print(f"Number of Games Won: {games_won}")
                    print(f"Number of Games Lost: {games_lost}")
                    print("-------------------")
                elif post_game_choice == "2":
                    break
                elif post_game_choice == "3":
                    print("Thank you for playing! Goodbye!")
                    return
                else:
                    print("Invalid choice. Please try again.")
        else:
            print("Invalid choice. Please try again.")

# Run the game
color_game()

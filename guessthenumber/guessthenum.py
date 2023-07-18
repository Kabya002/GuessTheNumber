import clear
import random
import logo
def guess_the_num():
    
        print(logo.logo)
        print("\n\nWelcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")

        chosen_num= random.randint(1,100)
        #print(f"Pssst, the correct answer is {chosen_num}")
        difficulty= input("Choose a difficulty. Type 'easy' or 'hard':")

        end_of_game= False
        if difficulty=='hard':
            guess=5
        if difficulty=='easy':
            guess=10
        print(f"You have {guess} attempts remaining to guess the number.")
            
        while not end_of_game:
            guess_num= int(input("Make a guess: "))
            if guess_num==chosen_num:
                print("You've won.")
                end_of_game=True
            if guess_num!=chosen_num:
                guess-=1
                if guess_num>chosen_num:
                    print("Too high.")
                if guess_num<chosen_num:
                    print("Too low.")
                if guess==0:
                    end_of_game= True
                    print("Game Over")
                    print(f"The number to be guessed was: {chosen_num}.")
        if input(f"Type 'y' to play again, or type 'n' to end game: ") == 'y':
            clear.clear()
            guess_the_num()
        else:
            print("Game over.")
            end_of_game=True
guess_the_num()

       
            
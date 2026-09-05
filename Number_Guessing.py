#    Number Guessing Game 
secret_number = int(input("Enter Secret Number: "))

print("\n"*10)

attempts = 0

print(" Number Guessing Game ")
print("I have thought of a number,Guess it!")


while True:
    try:
    
        user_guess = int(input("\nEnter Your Guess: "))
        attempts += 1
        
        
        if user_guess < secret_number:
            print("Too Low! Please Enter Bigger.")
        elif user_guess > secret_number:
            print("Too High! Please Enter Lower.")
        else:
            
            print(f"\n Congratulations! You Entered a Correct Number!")
            print("You Takes Total",attempts,"Attempts")
            break
            
    except ValueError:
        print("Please ek valid number enter karein!")

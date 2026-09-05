# Secure Password Validator

# Write a program that forces a user to enter a secure password. The while loop should keep asking for input until the user provides a string that meets all of these criteria:

# At least 8 characters long
# Contains at least one digit (0-9)
# Contains at least one special character (like $, #, or @)


password=input("Enter Your Password")
if len(password) >= 8:
    if "0" in password or "1" in password or "2" in password or "3" in password or "4" in password or "5" in password or "6" in password or "7" in password or "8" in password or "9" in password :
        if "$" in password or "#" in password or "@" in password :
            print("It's a Strong Password")
        else:
            print("It Does Not Contain Any Special Character")
    else:
        print("Password Does Not Have Any Number From 0-9")

else:
    print("Length Of Password Should Be Greater Than 8")
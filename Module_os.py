# isdir == folder
# ls shows the total files 
# lsfolder Shows the total folder
# lsfiles shows all the files
# exit type == stop the terminal

#   "OS.LISTDIR" sari ki sari file print kradega sb show krega file folder etc

import os

while True:

    command=input("-->>")

    if command == "exit":
        exit(0)

    elif command == "ls":
        all_file = os.listdir()
        for x in all_file:
            print(x)

    elif command == "lsfolder":
        all_file = os.listdir()
        for x in all_file:
            if os.path.isdir(x):
                print(x)

    elif command == "lsfiles":
        all_file = os.listdir()
        for x in all_file:
            if os.path.isfile(x):
                print(x)   

    elif command == "lspyfiles":
        all_file = os.listdir()
        for x in all_file:
            if os.path.isfile(x) and x.endswith(".py"):
                print(x)  

    elif command == "pwd":
        print(os.getcwd())   # GET CURRENT WORKING DIRECTORY 
 
    else:
        print("Invalid Command")
    
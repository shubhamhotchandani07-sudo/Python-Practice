def calculator(): 

    num1=float(input("Enter a number"))

    choice = input("Select Operation [ + | - | * | / | %] ➡️  ")

    num2=float(input("Enter a number"))
    # print("Operations + - * / %")

    if choice=="+":
        print(num1+num2)
        pass

    elif choice=="-":
        print(num1-num2)
        pass

    elif choice=="*":
            print(num1*num2)
            pass
    
    elif choice=="/":
            print(num1/num2)
            pass

    elif choice=="%":
            print(num1%num2)
            pass

    else:
          print("Inavlid Input Entered")

calculator()
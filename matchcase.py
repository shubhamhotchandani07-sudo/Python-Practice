month=int(input("Enter a number"))
match month:
    case 1|3|5|7|8|10|12:
        print("31 days")
    case 4|6|9|11:
        print("30 days")
    case 2:
        print("28 days")
    case _:
        print("Invalid input")


#WEEK DAYS MATCH CASE QUESTIONS

week=int(input("Enter a number"))
match week:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thrusday")
    case 5:
        print("Friday")
    case 6:
        print("Saturdy")
    case 7:
        print("Sunday")
    case _:
        print("Invalid Number Enter")

#TRAFFIC LIGHTS SIGNAL

character=input("Enter a character")
match character:
    case "red":
        print("Stop")
    case "yellow":
        print("Ready to stop or move")
    case "green":
        print("Go")
    case _:
        print("invalid input")
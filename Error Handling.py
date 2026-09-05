#   TRY , EXCEPT KEYWORD IS USED IN ERROR HANDLING

#Python me try aur except blocks ka use runtime errors (exceptions) ko handle karne aur program ko crash hone se 
#bachane ke liye kiya jata hai.

#Jab aapko lagta hai ki kisi code me error aa sakta hai, toh aap use try block me rakhte hain. Agar koi error aata hai, toh Python use catch karke except block ke code ko run kar deta hai

#ERROR tYPE:
# 1) KEY ERROR
# 2) VALUE ERROR
# 3) ZERO DIVISION ERROR
# 4) INDEX ERROR
# 5) TYPE ERROR
# 6) NAME ERROR
# 7) FILE NOT FOUND ERROR

#Finally block is also used in error handling Finally is run at botth condition in wrong or right both condition

try:
    number=int(input("Enter a number"))
except:
    print("please Enter Only Integers")


try:
    a=int(input("Enter a number"))
    b=int(input("Enter a number"))
    print(a*b)
except:
    print("There is an error from our side we are working on it")

try:
    a=int(input("Enter a number"))
    b=int(input("Enter a number"))
    print(a/b)
except ZeroDivisionError:
    print("You Cannot Divide Any Number By Zero")
except ValueError:
    print("please Enter Numbers Only")

#  FINALLY BLOCK
try:
    a=int(input("Enter a number 1:"))
    b=int(input("Enter a number 2:"))
    print(a/b)
except:
    print("Something if Wrong")
finally:
    print("I will run on both Case")

#  ELSE CONDITION IS ALSO USED IN ERROR HANDLING IT USED AND RUN WITH TRY CONDITION WITH TRUE CONDITION THT THERE IS NO ERROR
try:
    a=int(input("Enter a number"))
except:
    print("Type Conversion Error")
else:
    print("No Error")
finally:
    print("I Will Run In Both Conditions")

#  ELSE IS ALSO UED WITH LOOP
for x in range(5):
    print(x)
else:
    print("Else statement")


#User se 5 numbers input lo. Agar kisi input me text aa jaye to us input ko skip karo aur baaki numbers ka sum print karo.
try:
    a=int(input("Enter a number"))
    b=int(input("Enter a number"))
    c=int(input("Enter a number"))
    d=int(input("Enter a number"))
    e=int(input("Enter a number"))
    print(a+b+c+d+e)
except:
    print("Please Enter Integers Only!")
    

#WAP TO ASK THE USER TO ENTER A NUMBER AND HOE SHOULD PROGRAM HANDLE THE SITUATION IF USER ENTERS TEXT OR DECIMAL VALUE INSTEAD
try:
    a=int(input("Enter a number"))
    print(a,"\n""Yes Its Run Successfully")
except:
    print("Please Enter Integers Only Not Decimal or Text Value")


#CREATE A PROGRAM THAT DIVIDES THE TWO NUMBERS ENTERED BY THE USER. HOW SHOULD PROGRAM HANDLE DIVISION BY ZERO AND INVALID NUMERIC INPUT ?
try:
    a=int(input("Enter a number"))
    b=int(input("Enter a number"))
    print(a/b)
except ZeroDivisionError:
    print("Number Cannot Divide By Zero")
except ValueError:
    print("Invalid Numeric Entered, Please Entered Valid Numeric Value")


#CREATE A PROGRAM THAT ACCEPT A LIST INDEX FROM THE USER AND DISPLAYS THE CORRESPONDING ELMENT. HOW SHOULD THE PROGRAM HANDLE THE CASES WHERE THE INDEX IS OUT OF RANGE OR THE INPUT IS NOT A VALID INTEGER ?
list=[10,20,30,"Shubham",50,70]
try:
    i=int(input("Enter a index Value"))
    print(list[i])
except ValueError:
    print("Please Enter Valid Value")
except IndexError:
    print("Please Enter Valid Index value From 0 to 5")
#  Create a Circle class with the attribute radius. Write methods to calculate the area and circumference (perimeter) of the circle.
# class Circle:
#     radius = int(input("Enter a Radius"))

#     def area(self):
#         self.area = 3.14 * self.radius * self.radius
#         print(self.area)

#     def parameter(self):
#         self.parameter = 2 * 3.14 * self.radius
#         print(self.parameter)


# a = Circle()
# print(a.radius)
# a.area()
# a.parameter()


# Create a Rectangle class using a constructor to initialize length and width. Write methods to display the dimensions and calculate the area.
class Rectangle:

    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth

    def dimensions(self):
        print("Length:", self.length)
        print("Width:", self.breadth)

    def area(self):
        print("Area of Rectangle :", self.length * self.breadth)


b=Rectangle(10,5)
b.dimensions()
b.area()

#  Create a Student class. Accept student information using a constructor and write a method to calculate the total marks.

class student:

    
    def __init__(self):
        self.name="shubham"
        self.Roll_Number="25"
        self.Hindi=80
        self.English=75
        self.Maths=50
        self.Computer=90
        self.Science=65
        print(self.name)

    def methods(self):
        print(self.Hindi+self.Computer+self.English+self.Maths+self.Science)      

b=student()
b.methods()


#   Create a Mobile class using a constructor to initialize the brand, RAM, and storage. Write a method to print all specifications.
class Mobile:

    def __init__(self):
        self.Brand="Samsung"
        self.Ram=8
        self.Storage=128 

    def methods(self):
        print("Brand :",end="")
        print( self.Brand)
        print("Ram :",end="")
        print(self.Ram)
        print("Storage :",end="")
        print(self.Storage)

a=Mobile()
a.methods()


#  Create a BankAccount class with attributes account number, account holder name, and balance. Write methods to deposit and withdraw money.
class Bank_Account:

    account_number="2345678901"
    account_holder_name="Shubham"
    Balance=40000

    def deposit(self):
        self.Deposit=20000
        self.Withdraw=10000
        print("Deposit Money :",end="")
        print(self.Deposit)
        print("Withdraw Money :",end="")
        print(self.Withdraw)

    def total(self):
        print(self.Balance+self.Deposit-self.Withdraw)
    

a=Bank_Account()
a.deposit()
a.total()

#   Design a Calculator class that accepts two numbers using a constructor and performs arithmetic operations.
class Calculator:
    def __init__(self):
        num1=float(input("Enter a number"))
        choice = input("Select Operation (+,-,*,/,%) ")
            
        num2=float(input("Enter a number"))
                # print("Operations + - * / %")
            
        if choice=="+":
                    print(num1+num2)
                    
            
        elif choice=="-":
                    print(num1-num2)
                    
            
        elif choice=="*":
                        print(num1*num2)
                        
                
        elif choice=="/":
                        print(num1/num2)
                        
            
        elif choice=="%":
             print(num1%num2)
                        
            
        else:
              print("Inavlid Input Entered")
                
        
a=Calculator()
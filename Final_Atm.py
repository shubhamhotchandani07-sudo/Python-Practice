class Bank:

    def __init__(self,name,age,mob,dob,balance):
        self.name=name
        self.age=age
        self.mob=mob
        self.dob=dob
        self.balance=balance


    def Display_info(self):
        # print("Account Owner Name : ",end=-"")
        print("Name : ",self.name)
        # print("Account Owner Age : ",end=-"")
        print("Age : ",self.age)
        # print("Total Mobile Number : ",end=-"")
        print("Mobile Number : ",self.mob)
        # print("Owner dob : ",end=-"")
        print("Dob : ",self.dob)
        # print("Total Balance : ",end=-"")
        print("Balance : ",self.balance)


    def Deposit(self,amount):
        if amount>0:
            self.balance+=amount
        else:
            print("Invalid Amount Entered")


    def Withdraw(self,amount):
     if amount>0 and amount<=self.balance:
        self.balance-=amount
        print("Withdraw Successful. New Balance:",self.balance)
     else:
        print("Invalid Amount Entered / Insufficient Balance")

a=Bank("Shubham",19,"999",29,40000)

account=[]

while True:
    print("      'A. Create New Account" "\n"
"       B. Check Details" "\n"
"       C. Deposit Money" "\n"
"       D. Withdraw Money" "\n"
"       E. Exit '")


    choice=input("Enter Your Choice : ").upper()

    if choice=="A":
      name=input("Enter Your Name")
      age=int(input("Enter Your Age"))

      if age<18:
         print("Sorry Your Age is less than 18 Your Account Cannot be open")
      else:
         mob=input("Enter Your mob")
         dob=input("Enter Your dob")
         balance=int(input("Enter Your balance"))

         for x in account:
            if x.mob==mob:
               print("There is already Account Created Through This Number")
         account.append(Bank(name,age,mob,dob,balance))


    elif choice=="B":
     mob=input("Enter Your Mobile")

     for x in account:
        if x.mob==mob:
            x.Display_info()    
            break

    elif choice=="C":
         mob=input("Enter Your Mobile Number")
    
         for x in account:
            if x.mob==mob:
                amount=int(input("Enter a Amount : "))
                x.Deposit(amount)
                break

    elif choice == "D":
     mob=input("Enter Your Mobile Number")

     for x in account:
        if x.mob == mob:
            amount=int(input("Enter a Amount : "))
            x.Withdraw(amount)
            break

    elif choice=="E":
       exit(0)

    else:
       print("invalid Choice Entered Please Entered from A,B,C,D,E")


#  You define a child class by passing the parent class name inside parentheses (). This helps avoid writing duplicate code.
#  class ParentClass:
    # THIS IS PARENT CLASS

#class ChildClass(ParentClass):
    # THIS IS A CHILD CLASS

class Vehicle:

    brand = "Maruti"

class Car(Vehicle):
    pass

print(dir(Car))

print(Car.brand)


class hello:

    def __init__(self,name,brand):
        self.name=name
        self.brand=brand

class bye(hello):

    def __init__(self, name, brand):
        super().__init__(name, brand)

a=bye("Jeans","Levis")
print(a.name)
print(a.brand)
        

class Vehicle:

    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

def display_info(self):
        print(f"Brand: {self.brand}, Color: {self.color}")

class Car( Vehicle ):

    def wheels(self):
        print("Car has 4 wheels")

class Bus( Vehicle ):

    def wheels(self):
        print("Car has 10 wheels")


my_car = Car("Honda", "White")
print(my_car.brand)
print(dir(my_car))
my_car.wheels()

my_bus = Bus("Volvo", "Blue")
print(my_bus.color)
#my_bus.display_info()
my_bus.wheels()


# super(): Accessing the Parent Class
# The super() class is a special tool used to call methods from the parent class. This is particularly useful when the child class has its own __init__ method and you want to reuse the parent's initialization code


class Vehicle():

    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def display_info(self):
        print(f"Brand: {self.brand}, Color: {self.color}")

class Car( Vehicle ):

    def __init__(self, wheels):
        # Vehicle.__init__(self, "Honda", "White")
        super().__init__("Honda", "White")
        self.wheels = wheels

a = Car(4)
print(a.wheels)
a.display_info()
print(dir( a ))


class Vehicle:

    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
        print("Vehicle __init__ called.")

class Car(Vehicle):

    def __init__(self, num_wheels):
        self.num_wheels = num_wheels
        print("Car __init__ called.")
        super().__init__("Honda", "White")

    def car_info(self):
        print(f"This is a {self.color} {self.brand} with {self.num_wheels} wheels.")

my_car = Car(4)
print(my_car.num_wheels)
my_car.car_info()


# Method overriding is when a subclass provides its own specific implementation
#of a method that is already defined in its parent class.
#The method in the subclass "overrides" the one in the superclass.

class Vehicle:
    def display_info(self):
        print("This is a generic vehicle.")

class Car(Vehicle):
    # This method overrides the one in the parent class
    def display_info(self):
        print("This is a specific car.")

class Boat(Vehicle):
    pass

my_car = Car()
my_boat = Boat()
 
my_car.display_info()
my_boat.display_info() 

#  MULTIPLE LEVEL INHERITANCE

class mobile:

    def phone(self,Name,Model):
        self.Name=Name
        self.Model=Model
        print("This Provides the Name and Model Of Mobile")

class space:

    def space(self,Memory,Color):
        self.Memory=Memory
        self.Color=Color
        print("This Provides the Memory and Color Of Mobile")

class call(mobile,space):

    def battery(self):
        self.phone("Apple", 2025)
        self.space(8, "Orange")

a=call()
a.battery()
print(a.Name)
print(a.Model)
print(a.Memory)
print(a.Color)


# STUDENTS QUES ON MULTIULEVEL

class students:

    def person(self,name,age):
        self.name=name
        self.age=age

class Students:

    def Student(self,course,roll_no):
            self.course=course
            self.roll_no=roll_no

class result(students,Students):

    def marks(self):
        self.person("Shubham",18)
        self.Student("BCA",29)

b=result()
b.marks()
print(f"Name : {b.name}")
print(f"Age : {b.age}")
print(f"Course : {b.course}")
print(f"Roll_No : {b.roll_no}")

# CAR QUES ON MULTIULEVEL  
class Vehicle:

    def __init__(self,name):
        self.name=name

class gadi:

    def __init__(self,model):
        self.model=model

class sportscar(Vehicle,gadi):

    def __init__(self):
        Vehicle.__init__(self,"Virtus")
        gadi.__init__(self,2025)

c=sportscar()
print(f"Name : {c.name}")
print(f"Model : {c.model}")

# EMPLOYEE QUESTION
class Employee:

    def delloite(self,name,salary):
        self.name=name
        self.salary=salary

class Manager:

    def accenture(self,Department):
        self.Department=Department

class Director(Employee,Manager):

    def astegic(self,Company):
        Employee.delloite(self,"Shubham",200000)
        Manager.accenture(self,"Information Technology")
        self.Company=Company

c=Director()
c.astegic("Google")
print(f"Name : {c.name}")
print(f"Salary : {c.salary}")
print(f"Company : {c.Company}")


# father Mother multiple inheritence
class father:

    def Father_name(self,Name):
        self.Name=Name

    def father_business(self,business_name):
        self.business_name=business_name

class mother:

    def Mother_name(self,name):
        self.name=name

    def mother_job(self,job_name):
        self.job_name=job_name

class child(father,mother):

    def child_name(self):
        father.Father_name(self,"Shubham")
        father.father_business(self,"Clothes Business")

        mother.Mother_name(self,"Meena")
        mother.mother_job(self,"Housewife")

b=child()
b.child_name()
print(f"Father Name : {b.Name}")
print(f"Father Business : {b.business_name}")
print(f"Mother Name : {b.name}")
print(f"Mother Business : {b.job_name}")

class Personal_info:

    def __init__(self,name,age):
        self.name=name
        self.age=age

class college_info:

    def __init__(self,college,course):
        self.college=college
        self.course=course

class student(Personal_info,college_info):

    def __init__(self,name,age,college,course):
        Personal_info.__init__(self,name,age)
        college_info.__init__(self,college,course)

c=student("Shubham",20,"IPS","BCA")

print(f"Name : {c.name}")
print(f"Age : {c.age}")
print(f"College : {c.college}")
print(f"Course : {c.course}")


class light:

    def turn_on(self):
        print("Light is Turned On")

class Fan:

    def turn_on(self):
        print("Fan is Turned On")

class smartHome(light,Fan):

    def lockdoor(self):
        light.turn_on(self)
        Fan.turn_on(self)
        print("Locked The Door")
        
a=smartHome()
a.lockdoor()


# MULTILEVEL CLASS_INHERITENCE

class Grandparent:
    def show_grandparent(self):
        print("Grandparent")

class Parent(Grandparent):
    def show_parent(self):
        self.show_grandparent()
        print("Parent")

class Child(Parent):
    def show_child(self):
        print("Child")


a = Child()
a.show_child()
a.show_parent()

class animal:

    def tiger():
        print("Tiger")

class dog(animal):

    def lion():
        print("Lion")
        animal.tiger()

class puppy(dog):

    def cow(self):
        dog.lion()
        print("Puppy")

d=puppy()
d.cow()


class A:

    def Alphabet():
        print("a")

class B(A):

    def Alpha():
        A.Alphabet()
        print("b")

class C(B):

    def hello():
        B.Alpha()
        print("c")

class D(C):

    def bye(self):
        C.hello()
        print("D")

g=D()
g.bye()

class person:

    def gents():
        print("Gents")

class student(person):

    def lady():
        person.gents()
        print("Lady")

class college_student(student):

    def hello(self):
        student.lady()
        print("Hello")

n=college_student()
n.hello()


class a:

    def A(self):
        print("Aa")

class b(a):

    def B(self):
        a.A(self)
        print("Bb")
        c.C(self)

class c(b):

    def C(self):
        print("Cc")

k=b()
k.B()


class animal:

    def tiger():
        print("Tiger")

class dog():

    def lion():
        print("Lion")

class puppy(animal):

    def cow(self):
        animal.tiger()
        dog.lion()
        print("Puppy")

d=puppy()
d.cow()

#  HYBRID CLASS INHERITENCE

class employees:

    def name(self):
        print("Shubham")

class developer(employees):

    def Name(self):
        employees.name(self)
        print("Rohit")

class designer(employees):

    def naam(self):
        employees.name(self)
        print("Tushar")

class teamlead(developer,designer):

    def hello(self):
        developer.Name(self)
        designer.naam(self)
        print("kishu")

z=teamlead() 
z.hello()

class person:

    def aadmi(self):
        print("Shubham")

class student(person):

    def jaanwar(self):
        person.aadmi(self)
        print("kishu")

class gali(person):

    def BC(self):
        person.aadmi(self)
        print("MC")

class Assistant(student,gali):

    def manager(self):
        student.jaanwar(self)
        gali.BC(self)
        print("Boss")

x=Assistant()
x.manager()

class employee:

    def emplyee_name(self,name,id):
        self.name=name
        self.id=id

class developer(employee):

    def developer_language(self,language):
        employee.emplyee_name(self,"Shubham",29)
        self.language=language

class manager(employee):

    def damager(self,team_size):
        employee.emplyee_name(self,"Shubham",29)
        self.team_size=team_size

class teamlead(developer,manager):

    def display(self):
        developer.developer_language(self,"Python")
        manager.damager(self,20)

p=teamlead()
p.display()
print(f"Name : {p.name}")
print(f"ID : {p.id}")
print(f"Language : {p.language}")
print(f"team_size : {p.team_size}")

class person:

    def person_name(self,name,age):
        self.name=name
        self.age=age

class patient(person):

    def patient_diseases(self,disease):
        person.person_name(self,"Shubham",20)
        self.disease=disease

class doctor(person):

    def doctor_specialisation(self,specialization):
        person.person_name(self,"Shubham",20)
        self.specialization=specialization

class consultant(patient,doctor):

    def room(self,room_No):
        patient.patient_diseases(self,"Sugar")
        doctor.doctor_specialisation(self,"Sugar Specialist")
        

m=consultant()
m.room(20)
print(f"Name : {m.name}")
print(f"Age : {m.age}")
print(f"Disease : {m.disease}")
print(f"SpecialiZation : {m.specialization}")


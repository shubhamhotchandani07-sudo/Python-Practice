#   *args=arguments *=square ya remaining variables goes to a single varible
#    and *args print the output always inside the tuple

def args(a,*args):
    print(a)
    print(args)
args("apple","banana","cherry")


def string(a,b,c,d,e,f,*args):
    print(a,b,c,d,e,f,args)
string("HEllo","World","Shubham","Rohit","Tushar","Virat","Kohli","Boss","Mobile","jaduu","Bumrah","Calles")

def string(a="shubham",b="Rohit",c="Boss",d="kohli",*args):
    print(a,b,c,d,args)
string("World","Laptop","Print","Error","Input")

#    **kwargs   it gives output in dictionary not in tuple and it work with the key value pairs

def boss(**kwargs):
    print(kwargs)
boss(Name="Shubham",course="BCA",College="ABC",Mob="9530426834")

def car_info(**kwargs):
    print(kwargs)

car_info(brand="Tata", model="Nexon", year=2024)


def user_profile(**kwargs):
    print(kwargs)

user_profile(username="shubham_01", insta="shubham_ig", youtube="shubham_vlogs")


def laptop_specs(**kwargs):
    print(kwargs)

laptop_specs(ram="16GB", storage="512GB SSD", processor="i5")


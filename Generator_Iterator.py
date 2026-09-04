#Generator is a function that Acts Like An Iterator But It Defines As Yield Keyword Instead Of Return...

# GENERATOR OBJECT CALL BY WRITE      "NEXT"      IN PRINT FUNCTION IT CANNOT DIRECTLY PRINT 
# FOR EX -->>

# FUNCTION
def test():
    return 
    return 2
    return 3
    return 4

print(test)

# GENERATOR
def test():
    yield 1
    yield 2
    yield 3
    yield 4

abc=test()

print(next(abc))
print(next(abc))
print(next(abc))
print(next(abc))

# IF WE GIVE MORE PRINT FUNCTION IT GIVE STOP ITERATION ERROR..

#   SQUARE FUNCTION

def square(number):

    i=0
    while i<number:
        number=i*i
        i+=1
    return i*i
print(square(5))


def one_time():
    yield 1
    yield 2
    yield 3
    yield 4


for x in one_time():
    print(x)

def square(number):
    i=0
    while i<number:
        yield i*i
        i+=1

for x in square(5):
    print(x)


# def infinit_integer():
#     n=0
#     while True:
#         yield n
#         n+=1

# for x in infinit_integer():
#     print(x)


# EVEN NUMBER BY GENERATOR
def even(number):

    i=0
    while i<=number:
        if i%2==0:
            yield i
        i+=1

for x in even(10):
    print(x)

#   TABLE OF A NUMBER
def table(number):

    i=0
    while i<=10:
        yield number*i
        i+=1

for x in table(7):
    print(x)


# REVERSE OF NUMBER
def reverse():
    i=10
    while i>0:
        yield i
        i-=1

for x in reverse():
    print(x)

#  VOWELS
def vowels():
    a = "Programming"

    for x in a:
        if x in "AEIOUaeiou":
            yield x

for x in vowels():
    print(x)

def check():

    def checker():
    digit = [-5, 10, -2, 8, 0, -7, 15]

    for x in check:
        if x > 0:
            yield x

for x in check():
    print(x)

# SQUARE OF EVEN NUMBERS
def even(number):

    i=0
    while i<=number:
        if i%2==0:
            yield i*i
        i+=1

for x in even(10):
    print(x) 
#How do you find the total no of unique element inside the set
#it complete by len function and it count simgle element if a element repeats in a set
#FOR EXAMPLE-
a={10,20,30,50,50,50,70,60}
print(len(a))

a={1,2,3,4,5,6,7,8}
print(dir(a))

#GIVEN TWO SETS HOW DO YOU FINS THE ELEMENTS COMMON TO BOTH
a={1,2,3,4,5,6,7}
b={7,8,9,10,11,12}
print(a.intersection(b))

#HOW DO YOU ADD A SINGLE ELEMENT AND MULTIPLE ELEMENT AT ONCE IN SETS IN PYTHON
a={1,2,3}
a.add(4)
print(a)

a={1,2,3}
a.update([4,5,6])
print(a)

#GIVEN TWO SETS HOW DO YOU GET ALL THE UNIQUE ELEMENT FROM BOTH COMBINED
#UNION IS USED TO COMPLETE THIS QUESTION 
a={1,2,3,4,5,6,7}
b={1,9,3,7,10,11}
print(a.union(b))

#HOW DO YOU REMOVE AN ELEMENT WITHOUT RAISING AN ERROR IF IT DOESNT EXISTS 
a={1,2,3,4,4,4,5,6}
a.discard(4)
print(a)

#HOW DO YOU CHECK IF ONE SET IS COMPLETELY CONTAINED SUBSET OF ANOTHER
a={1,2}
b={1,2,3,4}
result= a.issubset(b)
print(result)

#HOW DO YOU REMOVE ALL ELEMENTS TO MAKE A SET EMPTY
a={1,2,3,4,5,6,7,8,9,"shubham"}
a.clear()
print(a)
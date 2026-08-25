class Personal_info:

    def __init__(self,name,age):
        self.__name=name
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
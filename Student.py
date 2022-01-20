class Student:
    college = "KLU"
    '''docstring for ClassName'''

    def __init__(self, id,name,course):
        #super().__init__(self,id,name,course)
        # self.arg=arg
        self.id = id
        self.name = name
        self.course = course

    def display(self):
        print(f"this is {self.id}")
        print(f"this is {self.name}")
        print(f"this is {self.course}")


s1 = Student(1234, "abc", "CSE")
# s1=instance(don't call object)
print(s1)
s1.display()
print(s1.college)
print(Student.college)

#Create a class called as prouct with id, quantity, name, price and with two methods dispaly of products and display of bill,
# craete two instances/objects(use fstring)
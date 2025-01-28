class Person:
    def __init__(self, name, id_number):
        self.name = name
        self.id_number = id_number
    def display(self):
        print(self.name)
        print(self.id_number)


class Student(Person):
    def __init__(self, name, id_number, grade):
        self.grade = grade
        super().__init__(name, id_number)
name = input("Enter your name : ")
id_number =int(input("Enter your id number : "))
grade = int(input("Enter your grade : "))

obj = Student(name, id_number, grade)
obj.display()
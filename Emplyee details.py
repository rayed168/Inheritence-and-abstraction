class Employer:
    def __init__(self, name, id_number):
        self.name = name
        self.id_number = id_number
    def display(self):
        print(self.name)
        print(self.id_number)


class Emplyee(Employer):
    def __init__(self, name, id_number, salary, post):
        self.salary = salary
        self.post = post
        Emplyee.__init__(self, name, id_number)
name = input("Enter your name : ")
id_number =int(input("Enter your id number : "))
salary = input("Enter your salary : ")
post = input("Enter your post : ")

obj = Emplyee(name, id_number, salary, post)
obj.display()
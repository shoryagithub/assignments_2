class person:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"Hello, my name is {self.name}.")
        return self.name

m1 = person("Shorya")
m1.show()

class Employee(person):
    def __init__(self, name ,salary):
        super().__init__(name)
        self.salary = salary

    def show(self):
        super().show()
        print(f"My salary is {self.salary}.")
        
m2 = Employee("Shorya", 50000)
m2.show()

class Project_manager(Employee):
    def __init__ (self, name, salary, project):
        super().__init__(name, salary)
        self.project = project

    def show(self):
        super().show()
        print(f"I am managing the project: {self.project}.")

    def show_project(self):
        print(f"Project: {self.project}")
    
m3 = Project_manager("Shorya", 50000, "AI Development")
m3.show()
m3.show_project()

class iterator:
    def __init__(self, numbers):
        self.numbers = numbers
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.numbers):
            value = self.numbers[self.index]
            self.index += 1
            return value
        else:
            raise StopIteration

for val in iterator([1, 2, 3, 4, 5]):
    print(val)

def generator_function():
    for i in range(5):
        yield i * 2

for val in generator_function():
    print(val)

def outer(message):
    def inner():
        print("This is the inner closure")
    return inner

show = outer("Hello from shorya closer")
show()

def my_decorator(func):
    def wrapper():
        print("the function before")
        func()
        print("the After function")
    return wrapper

def greet():
    print("Hello, I am Shorya Agrawal")

greet()


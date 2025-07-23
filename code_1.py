import re  # For Regular Expression

# === Closure ===
def make_closure():
    message = "Hello from Closure"
    def inner():
        print(message)
    return inner

# === Decorator ===
def simple_decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper

@simple_decorator
def greet():
    print("Hello!")

# === Base Class for Inheritance ===
class Animal:
    def speak(self):
        print("Animal speaks")

# === Another Base Class for Multiple Inheritance ===
class Walker:
    def walk(self):
        print("I can walk")

# === Main Class that shows all OOP Concepts ===
class MyClass(Animal, Walker):
    def __init__(self, name):
        self.name = name
        self.numbers = [1, 2, 3]
        self.index = 0
        self._value = 0  # For property demo

    # === Operator Overloading ===
    def __add__(self, other):
        return self.name + other.name

    # === Iterator ===
    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.numbers):
            val = self.numbers[self.index]
            self.index += 1
            return val
        else:
            raise StopIteration

    # === Generator ===
    def my_generator(self):
        for n in self.numbers:
            yield n * 10

    # === Property ===
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, v):
        self._value = v

    # === Class Method ===
    @classmethod
    def say_class(cls):
        print("This is a class method")

    # === Static Method ===
    @staticmethod
    def say_static():
        print("This is a static method")

    # === Regex ===
    def show_numbers_in_text(self, text):
        found = re.findall(r'\d+', text)
        print("Numbers found using regex:", found)

# === Using the Decorator ===
print("=== Decorator ===")
greet()

# === Using the Closure ===
print("\n=== Closure ===")
closure = make_closure()
closure()

# === Creating Object ===
print("\n=== Creating Object ===")
obj = MyClass("Tom")
obj2 = MyClass("Jerry")

# Inheritance and Multiple Inheritance
print("\n=== Inheritance ===")
obj.speak()
obj.walk()

# Operator Overloading
print("\n=== Operator Overloading ===")
print("Result of obj + obj2:", obj + obj2)

# Iterator
print("\n=== Iterator ===")
for i in obj:
    print(i)

# Generator
print("\n=== Generator ===")
for g in obj.my_generator():
    print(g)

# Property
print("\n=== Property ===")
obj.value = 100
print("Property value is:", obj.value)

# Class Method and Static Method
print("\n=== Class and Static Methods ===")
MyClass.say_class()
MyClass.say_static()

# Regex
print("\n=== RegEx ===")
obj.show_numbers_in_text("My phone number is 9876543210 and pin is 462001")
print("End of the code execution.")
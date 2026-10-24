# class Father:
#     eye_color = "brown"

#     def sing(self):
#         print("Can sing")

# class Mother:
#     hair_color = "blonde"

#     def dance(self):
#         print("Can dance")

# class Child(Father, Mother):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def talk(self):
#         print(f"Hi, my name is {self.name} and I am {self.age} years old")


# c = Child('John', 23)
# print(c.eye_color)
# print(c.hair_color)
# c.sing()
# c.dance()
# c.talk()


class GrandFather:
    # def represent(self):
    #     print("grandfather")
    pass


class Father(GrandFather):
    def __init__(self, eye_color):
        self.eye_color = eye_color

    def sing(self):
        print("Can sing")

    # def represent(self):
    #     print("father")


class Mother:
    def __init__(self, hair_color):
        self.hair_color = hair_color

    def dance(self):
        print("Can dance")

    def represent(self):
        print("mother")


class Child(Father, Mother):
    def __init__(self, eye_color, hair_color, name, age):
        # super().__init__(eye_color, hair_color)
        Mother.__init__(self, hair_color)
        Father.__init__(self, eye_color)
        self.name = name
        self.age = age

    def talk(self):
        print(f"Hi, my name is {self.name} and I am {self.age} years old")

    def represent(self):
        print("child")


c = Child("green", "black", "John", 24)
print(c.eye_color)
print(c.hair_color)
c.represent()
print(Child.__mro__)


class A:
    def method(self): print("A")
class B(A):
    def method(self): print("B")
class C(A):
    def method(self): print("C")
class D(B, C):
    pass 

print(D.__mro__)

#      A
#     / \
#    B   C
#     \ /
#      D



from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    def perimeter(self):
        print("Perimeter")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2
    
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height


circle_1 = Circle(5)
print(circle_1.area())

rec = Rectangle(5, 10)
print(rec.area())


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __call__(self):
        print("This is __call__ method")
 
    def __str__(self):
        return f"{self.x}, {self.y}"
    
    def __repr__(self):
        return f"Vector ({self.x}, {self.y})"

vector_1 = Vector(1, 2)
print(vector_1)
print(repr(vector_1))

vector_1()


test = frozenset({1, 2, 3})
print(test)

# gt - greater than
# ge/gte - greater than or equal to



class PositiveNumber:
    """Enforces positive numeric values"""
    def __init__(self, name):
        self.name = f"_{name}"

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError(
                f"{self.name} must be positive"
            )
        setattr(instance, self.name, value)

    def __delete__(self, instance):
        raise AttributeError(
            "Cannot delete attribute"
        )


class BankAccount:
    balance = PositiveNumber("balance")
    credit_limit = PositiveNumber("credit_limit")

    def __init__(self, balance=0,
                 credit_limit=1000):
        self.balance = balance
        self.credit_limit = credit_limit

acc = BankAccount(500)
print(acc.balance)   # 500
acc.balance = 100 
print(acc.balance)   

print(acc.__dict__)


class FileManager:
    def __init__(self, file_name, mode):
        self.file_name = file_name
        self.mode = mode

    def __enter__(self):
        print("Entering")
        self.file = open(self.file_name, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting")
        self.file.close()

with FileManager("test.txt", "w") as f:
    f.write("Hello, world!")


print("Done")



from datetime import datetime

class BankingError(Exception):
    """Base class for all banking-related errors."""
    def __init__(self, message, account_id=None):
        super().__init__(message)
        self.account_id = account_id
        self.timestamp = datetime.now()


def main(balance):
    if balance < 0:
        raise BankingError("Balance cannot be negative")
    
# main(-100)

try:
    main(-100)

except BankingError as e:
    print(e)
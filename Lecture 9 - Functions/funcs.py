count = 0
for i in "Python":
    count += 1

print(count)

print(len("Python"))


import time
print(time.time())


def calculate_sum():
    """
    This function adds two numbers and prints the result.
    """
    print(5 + 3)

calculate_sum()


def add():
    x = 5
    y = 3
    print(x + y)

add()
add()
add()
print("Hello")
add()


def calculate():
    x = 5
    y = 3
    print(x + y)

calculate()


def sum_calculator(x, y):
    print(f"x - {x}, y - {y}")
    print(x + y)

sum_calculator(5, 3)
sum_calculator(10, 4)


# def full_name(first_name, last_name):
#     print(f"{first_name} {last_name}")

# full_name("John", "Doe")
# full_name(last_name="Doe", first_name="John")


def print_full_name(first_name, last_name, age, status="student"):
    print(f"{first_name} {last_name}")
    print(f"Age: {age}, Status: {status}")

f_name = input("Enter your first name: ").capitalize()
l_name = input("Enter your last name: ").capitalize()

print_full_name(f_name, l_name, status="teacher", age=25)


# def append_item(item, lst=[]): # wrong way
#     lst.append(item)

#     print(lst)

# append_item("Python")
# append_item("Java")
# append_item(["C++", "C#", "JavaScript"])



def append_item(item, lst=None):
    if lst is None:
        lst = []
    
    lst.append(item)

    print(lst)

append_item("Python", ["C++", "C#", "JavaScript"])
append_item("Java")


print(append_item("Python"))


def full_name(first_name, last_name):
    return f"{first_name} {last_name}"

f_name =input("Enter your first name: ").capitalize()
l_name = input("Enter your last name: ").capitalize()

print(full_name(f_name, l_name))

name = full_name(f_name, l_name)
print(name)


def greeting(full_name):
    return f"Hello, {full_name}"

print(greeting(name))




def check_age(age):
    if age < 0:
        return "Invalid age"
    
    print("after first IF")
    
    if age < 18:
        return "You are younger than 18"
    else:
        return "You are older than 18"
    
    
print(check_age(-10))
print(check_age(15))



def divmod(a, b):
    return a // b, a % b

print(divmod(10, 3))

floor_division, modulus = divmod(10, 3)

print(floor_division)
print(modulus)

x = 10

def sum():
    x = 5
    y = 3
    return x + y

print(x)


def student_info(name, age, *args):
    return f"{name} is {age} years old, {args}"

print(student_info("John", 20, "City - Tbilisi", "Hobby - Reading", "Learning - Programming", 2001))



def student(name, age, *args, **kwargs):
    return f"{name} is {age} years old, {args}, {kwargs}"

print(student("John", 20, "Reading", "Programming", city="Tbilisi", year=2001))



# from random import randint


def create_profile(first_name):
    return {
        "first_name": first_name
    }
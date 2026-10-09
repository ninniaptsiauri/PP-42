# def outer():
#     print("Outer Function")

#     def inner():
#         # print("Inner Function")
#         return "Inner Function"

#     return inner()

# print(outer())

x = "Global Variable"

def outer():
    x = "Enclosing Variable"
    print(x)
    # print("Outer Function")

    def inner():
        # x = "Local Variable"
        # nonlocal x
        global x
        x += "hello"
        print(x)
        # print("Inner Function")

    inner()

outer()
print(x)



def counter():
    count = 0

    print("Counter Function")

    count += 1

    return count

print(counter())
print(counter())
print(counter())
print(counter())
print(counter())


def make_counter():
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count
    
    return counter

counter1 = make_counter()

print(counter1())
print(counter1())
print(counter1())
print(counter1())
print(counter1())
print(counter1())



def make_multiplier(factor):
    def multiplier(x):
        return x * factor  # 'factor' is remembered
    return multiplier

double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))  # 10
print(triple(5))  # 15


def my_decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")

    return wrapper

@my_decorator
def print_hello():
    print("Hello")
    print("How are you?")

print_hello()

@my_decorator
def sum():
    print(2 + 3)

sum()


# hello = my_decorator(print_hello)
# hello()


import time

def timer_func(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} took {end_time - start_time:.2f} seconds")
        return result
    
    return wrapper

@timer_func
def calculates_sum(a, b):
    time.sleep(2)
    print(a + b)


calculates_sum(2, 3)



def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Function {func.__name__} was called")
        print(f"Args: {args}")
        print(f'Kwargs: {kwargs}')

        return func(*args, **kwargs)
    
    return wrapper


@logger
def calculate_sum(a, b, operation):
    return a + b
        

print(calculate_sum(2, 3, operation="add"))


from functools import wraps

def repeat(times=3):
    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        
        return wrapper
    
    return decorator


@repeat(5)
def say_hello():
    """This function says hello"""
    print("Hello")


# say_hello()
print(f"Name: {say_hello.__name__}, Docs: {say_hello.__doc__}")

import time

def timer(performance_time=2.0):
    def decorator(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()

            execution_time = end_time - start_time

            print(f"Function {func.__name__} took {execution_time:.2f} seconds")

            if execution_time > performance_time:
                print("Function took too long")

            else:
                print("Function took too short")
            
            return result
        
        return wrapper
    
    return decorator


@timer()
def divide(a, b):
    time.sleep(1)
    return a / b

@timer(performance_time=1.0)
def modulus(a, b):
    time.sleep(1)
    return a % b


print(divide(10, 2))

print(modulus(10, 2))
def generator_func(num):
    while True:
        if num == 0:
            break

        yield num
        num -= 1


func = generator_func(3)
print(next(func))
print(next(func))
print(next(func))
print(next(func))

for item in func:
    print(item)



def odd_nums():
    num = 1

    while True:
        yield num
        num += 2

func = odd_nums()

print(next(func))
print(next(func))
print(next(func))
print(next(func))



import sys

squares_list = [x * x for x in range(1000)]
squares_gen = (x * x for x in range(1000))

print(squares_list)
print(squares_gen)

print(next(squares_gen))
print(next(squares_gen))
print(next(squares_gen))

for item in squares_gen:
    print(item)


list_memory = sys.getsizeof(squares_list)
gen_memory = sys.getsizeof(squares_gen)

print(list_memory)
print(gen_memory)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_nums = filter(lambda num: num % 2 == 0, numbers)
print(even_nums)

for num in even_nums:
    print(num)


def accumulator():
    total = 0

    while True:
        value = yield total

        if value is None:
            break

        total += value


acc = accumulator()
print(next(acc))
print(acc.send(10))
print(acc.send(20))
print(acc.send(30))


def generator_1():
    yield "A"
    yield "B"

def generator_2():
    yield "C"
    yield "D"

def generator_3():
    yield "E"
    yield "F"

# Old way
# def combined_generator():
#     for item in generator_1():
#         yield item

#     for item in generator_2():
#         yield item


def combined_generator():
    yield from generator_1()
    yield from generator_2()
    yield from generator_3()


for item in combined_generator():
    print(item)



import time
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"{func.__name__} completed in {elapsed:.4f}s")
        return result
    return wrapper

@timer
def process_large_data():
    # Generator expression inside — memory efficient
    return sum(x*x for x in range(1_000_000))

process_large_data()
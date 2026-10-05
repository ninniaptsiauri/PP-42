def calculate_sum(*args):
    total = 0
    for num in args:
        total += num
    return total

print(calculate_sum(2, 6))
print(calculate_sum(2, 6, 10, 20, 15))


def student_info(**kwargs):
    
    return kwargs

print(student_info(name="John", age=20, city="Tbilisi"))


#  5 * 4 * 3 * 2 * 1 = 120

def factorial(n):
    if n == 0:
        return 1
    
    return n * factorial(n - 1)

    for i in range(1, n):
        n *= i

    return n

print(factorial(5))
print(factorial(4))



def square(x):
    return x ** 2

print(square(5))
print(square)

square_result = square(4)

square_lambda = lambda x: x ** 2
print(square_lambda(5))


lst = [1, 8, 5, 2, 3, 9, 4, 7, 6]

sorted_lst = sorted(lst)
print(sorted_lst)

sorted_lst = sorted(lst, reverse=True)
print(sorted_lst)


students = [
    ("John", 85),
    ("Anna", 90),
    ("Bob", 75),
    ("Alice", 92)
]

sorted_students = sorted(students, key=lambda student: student[1])
print(sorted_students)


def sort_student(student):
    return student[1]

sorted_students = sorted(students, key=sort_student, reverse=True)
print(sorted_students)


people = [
    ("John", 20, 85),
    ("Anna", 21, 90),
    ("Bob", 20, 75),
    ("Alice", 21, 92)
]

sorted_people = sorted(people, key=lambda person: (person[1], person[2]), reverse=True)
print(sorted_people)


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
mapped_nums = list(map(lambda num: num * 2, nums))
mapped_nums = list(map(lambda num: num * 2 if num % 2 == 0 else num, nums))
print(mapped_nums)


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_nums = list(filter(lambda num: num % 2 == 0, nums))
print(filtered_nums)


def even_nums(num):
    return num % 2 == 0

filtered_nums = list(filter(even_nums, nums))
print(filtered_nums)

from functools import reduce

lst = [1, 2, 3, 4, 5, 6, 7, 8]
sum_of_nums = reduce(lambda acc, num: acc + num, lst)
print(sum_of_nums)


student_names = ["John", "Anna", "Bob"]
student_scores = [85, 90, 75, 77, 91]

student_info = list(zip(student_names, student_scores))
print(student_info)


student_names = ["John", "Anna", "Bob", "Alice"]
student_scores = [85, 90, 75, 77, 91]
cities = ["Tbilisi", "Batumi", "Kutaisi", "Rustavi"]

student_infos = list(zip(student_names, student_scores, cities))
print(student_infos)


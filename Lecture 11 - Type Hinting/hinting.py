age: int = 25
print(type(age))

name: str = "John"
print(type(name))


def full_name(first_name: str, last_name: str) -> str:
    return first_name.capitalize() + last_name.capitalize()

f_name = full_name("john", "doe")
print(f_name)

# f_name = full_name(10, 20)
# print(f_name)

scores: list[int] = [1, 2, 3]
print(scores)
print(type(scores))

student_info: dict[str, str] = {"name": "John", "age": "20"}
print(student_info)
print(type(student_info))

nums: tuple[int, int, int, int] = (1, 2, 3, 4)
print(nums)
print(type(nums))


user_name: str | None = None

from typing import Any

first_name: Any = []


student: dict[str, str | int] = {"name": "John", "age": 20}
print(student)
print(type(student))



def add_nums(a, b):
    print(a + b)

print(add_nums(1, 2))
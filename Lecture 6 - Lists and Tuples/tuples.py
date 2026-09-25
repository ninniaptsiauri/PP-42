empty_tuple = ()
print(type(empty_tuple))

numbers = (1, 2, 3)
print(numbers)

fruits = ("apple", "banana", "cherry")

for fruit in fruits:
    print(fruit)


student = ("John", 20, "Tbilisi")
name, age, city = student
print(name)
print(age)
print(city)


students = (("John", 20, "Tbilisi"), ("Anna", 21, "Batumi"))
for name, age, city in students:
    print(name)
    print(age)
    print(city)

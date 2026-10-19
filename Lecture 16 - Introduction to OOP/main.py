class Car:
    wheels_count = 4
    steering_wheel = 1

    def __init__(self, brand_name, color):
        self.brand_name = brand_name
        self.color = color

    def start(self):
        print(f"{self.brand_name} started")

    def stop(self):
        print("Car stopped")

    def turn_left(self):
        print("Car turned left")

    def turn_right(self):
        print("Car turned right")

Car.steering_wheel = 2

car_1 = Car("BMW", "Black")
print(type(car_1))
print(id(car_1))
print(car_1.wheels_count)
print(car_1.steering_wheel)
car_1.start()
car_1.stop()
car_1.turn_left()
car_1.turn_right()
print(car_1.brand_name)
print(car_1.color)
car_1.wheels_count = 3
print(car_1.wheels_count)
car_1.color = "Red"
print(car_1.color)

print("=" * 40)

car_2 = Car("Mercedes", "White")
print(type(car_2))
print(id(car_2))
print(car_2.wheels_count)
print(car_2.steering_wheel)
car_2.start()
car_2.stop()
car_2.turn_left()
car_2.turn_right()
print(car_2.brand_name)
print(car_2.color)
print(car_2.wheels_count)
car_2.brand_name = "BMW"
print(car_2.brand_name)

num = 10
print(type(num))



class Student:
    university = "IT Academy Step"

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.courses = []
        self.gpa = 0
        self.year = 1

    def add_course(self, course):
        if course not in self.courses:
            self.courses.append(course)
        
        else:
            print(f"{course} is already added")



    def display(self):
        print("=" * 40)
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"University: {self.university}")
        print(f"Courses: {self.courses}")
        print(f"GPA: {self.gpa}")
        print(f"Year: {self.year}")


print("=" * 40)
student1 = Student("John", 20)
student1.add_course("Python")
student1.add_course("Java")
student1.add_course("Java")
student1.display()
print(student1.name)
print(student1.age)
print(student1.university)

print("=" * 40)
student2 = Student("Anna", 21)
student2.display()
print(student2.name)
print(student2.age)
print(student2.university)

print("=" * 40)
student3 = Student("Bob", 22)
student3.display()
print(student3.name)
print(student3.age)
print(student3.university)


student_list = [
    (1, "John", 22),
    (2, "Anna", 21),
    (3, "Bob", 20)
]

student_object_list = []

for student in student_list:
    s = Student(student[1], student[2])
    student_object_list.append(s)

print(student_object_list)

for student in student_object_list:
    if student.age > 21:
        student.add_course("C++")

    if student.gpa > 3.5:
        student.add_course("C#")

    student.display()



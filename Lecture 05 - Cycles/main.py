# ######################################
# # While Loops
# ######################################

count = 0  # 0 1 2 3 4 5
while count < 5:
    print(count)  # 0 1 2 3 4
    count += 1


i = 5     # 5 4 3 2 1 0
while i > 0:
    print(i)
    i -= 1


password = ""
tries = 0

while password != "Python" and tries < 3:
    password = input("Please enter your password: ")
    tries += 1

if password != "Python" and tries == 3:
    print("You entered the wrong password 3 times")
else:
    print("You entered the correct password")
    

age = -1
while age < 0 or age > 120:
    age = int(input("Please enter your age: ")) 

print(f"You are {age} years old")


i = 1
total = 0 # +1 +2 +3 +4 +5 = 15

while i <= 5:
    total += i 
    i += 1

print(total)



######################################
# While True
######################################

while True:
    text = input("Please enter your text: ").strip().lower()

    if text == 'exit':
        print("Exiting...")
        break



i = 0

while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)     # 1 2 4 5


# ######################################
# # Nested While Loops
# ######################################

row = 1
while row <= 4:
    col = 1
    while col <= 3:
        print("*", end=" ")
        col += 1
    print()
    row += 1

# * * * 
# * * * 
# * * * 
# * * *



######################################
# For Loops
######################################

print("y" in "Python")

for i in "Python Programming":
    print(i)


for i in range(5): # 0 1 2 3 4
    print(i)


for i in range(5, 11):
    print(i)

for i in range(5, 11, 2):
    print(i)

for i in range(10, 4, -1):
    print(i)


total = 0

for i in range(1, 6):
    total += i

print(total)


for i in range(1, 6):
    if i == 3:
        break
    print(i)


for i in range(1, 6):
    if i == 3:
        continue
    print(i)  # 1 2 4 5


######################################
# Nested For Loops
######################################

for row in range(4): # 0 1 2 3
    for col in range(3): # 0 1 2 
        print("*", end=" ")
    print()

# * * *
# * * *
# * * *
# * * *
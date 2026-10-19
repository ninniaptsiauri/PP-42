# file = open("test.txt", "r")
# data = file.read()

# print(data)

# line = file.readline()

# print(line)


# lines = file.readlines()

# print(lines)

# file.close()

# file.read()



# file = open("create_file.txt", 'x')

# file.close()


# file = open("text.txt", 'w')

# # file.write("Hello World")

# lst = ["Banana\n", "Grape\n", "Apple"]

# file.writelines(lst)

# file.close()

# lst = ["Python\n", "Java\n", "C++\n"]

# file = open("text.txt", "a")

# file.writelines(lst)

# file.read()

# print(file.readable())

# print(file.writable())

# file.close()


# file = open("text.txt", "r+")
# # print(file.readable())
# # print(file.writable())

# file.write("Hello World")

# file.close()


# file = open("text.txt", "rb")
# # print(file.readable())
# # print(file.writable())

# file.write("Hello World")

# file.close()


# with open("text.txt", "r") as file:
#     data = file.read()

#     print(data)

# print("File closed")
# file.read()


# with open("text.txt", "a") as file:
#     file.write("\nPython Programming")


try:
    with open("tex.txt", "r") as file:
        data = file.read()

        print(data)

except FileNotFoundError:
    print("File not found")
import csv

# with open("data.csv", "r") as file:
#     reader = csv.reader(file)

#     for row in reader:
#         print(row)


# people = [
#     ["John", 20],
#     ["Anna", 21],
#     ["Bob", 20],
#     ["Alice", 21]
# ]

# with open("test.csv", "w") as file:
#     writer = csv.writer(file)

#     writer.writerow(["Name", "Age"])

#     writer.writerows(people)


# with open("data.csv", 'r') as file:
#     reader = csv.DictReader(file, delimiter=",")

#     for row in reader:
#         print(row)

# headers = ["id", "name", "age"]
# people = [
#     {"id": 1, "name": "John", "age": 20},
#     {"id": 2, "name": "Anna", "age": 21},
#     {"id": 3, "name": "Bob", "age": 20},
#     {"name": "Alice", "id": 4, "age": 21}
# ]

with open("data.csv", "w") as file:
    writer = csv.DictWriter(file, fieldnames=headers, delimiter="\t")

    writer.writeheader()

    writer.writerows(people)


# with open("data.csv", "r") as file:
#     reader = csv.DictReader(file, delimiter="\t")

#     for row in reader:
#         print(row)